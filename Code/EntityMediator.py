from Code.Const import WIN_WIDTH
from Code.EnemyShot import EnemyShot
from Code.Entity import Entity
from Code.Enemy import Enemy
from Code.PlayerShot import PlayerShot


class EntityMediator:

    @staticmethod
    def __verify_collision_window(ent: Entity):
        if isinstance(ent, Enemy):
            if ent.rect.rigth <= 0:
                ent.health = 0
        if isinstance(ent, PlayerShot):
            if ent.rect.left > WIN_WIDTH:
                ent.health = 0
        if isinstance(ent, EnemyShot):
            if ent.rect.rigth <= 0:
                ent.health = 0

    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        for i in range(len(entity_list)):
            test_entity = entity_list[i]
            EntityMediator.__verify_collision_window(test_entity)

    @staticmethod
    def verify_health(entity_list: list[Entity]):
        for ent in entity_list:
            if ent.health <= 0:
                entity_list.remove(ent)

