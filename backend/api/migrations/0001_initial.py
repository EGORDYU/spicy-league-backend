# api/migrations/0001_initial.py
from django.db import migrations, models
import django.db.models.deletion

def set_default_user(apps, schema_editor):
    User = apps.get_model('auth', 'User')
    Player = apps.get_model('api', 'Player')
    default_user = User.objects.get(username='egordyu')
    for player in Player.objects.all():
        if not player.user_id:
            player.user = default_user
            player.save()

class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),  # Adjust this to match your auth migrations
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('starcraftrank', models.CharField(choices=[('bronze', 'Bronze'), ('silver', 'Silver'), ('gold', 'Gold'), ('platinum', 'Platinum'), ('diamond', 'Diamond'), ('master', 'Master'), ('grandmaster', 'Grandmaster'), ('n/a', 'N/A')], default='n/a', max_length=100)),
                ('starcraftrace', models.CharField(choices=[('terran', 'Terran'), ('zerg', 'Zerg'), ('protoss', 'Protoss'), ('n/a', 'N/A')], default='n/a', max_length=100)),
                ('leaguerank', models.CharField(choices=[('iron', 'Iron'), ('bronze', 'Bronze'), ('silver', 'Silver'), ('gold', 'Gold'), ('platinum', 'Platinum'), ('emerald', 'Emerald'), ('diamond', 'Diamond'), ('master', 'Master'), ('grandmaster', 'Grandmaster'), ('challenger', 'Challenger'), ('n/a', 'N/A')], default='n/a', max_length=100)),
                ('leaguerole', models.CharField(choices=[('top', 'Top'), ('jungle', 'Jungle'), ('mid', 'Mid'), ('adc', 'ADC'), ('support', 'Support'), ('fill', 'Fill'), ('n/a', 'N/A')], default='n/a', max_length=100)),
                ('leaguesecondaryrole', models.CharField(choices=[('top', 'Top'), ('jungle', 'Jungle'), ('mid', 'Mid'), ('adc', 'ADC'), ('support', 'Support'), ('fill', 'Fill'), ('n/a', 'N/A')], default='n/a', max_length=100)),
                ('cs2elo', models.IntegerField(choices=[(i, str(i)) for i in range(0, 30001, 1000)], default=0)),
                ('profimage', models.CharField(default='https://t4.ftcdn.net/jpg/00/64/67/27/360_F_64672736_U5kpdGs9keUll8CRQ3p3YaEv2M6qkVY5.jpg', max_length=255)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='players', to='auth.user')),
            ],
        ),
        migrations.RunPython(set_default_user),
    ]
