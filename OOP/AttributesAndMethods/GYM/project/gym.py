class Gym:

    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer):
        if customer.id not in [c.id for c in self.customers]:
            self.customers.append(customer)

    def add_trainer(self, trainer):
        if trainer.id not in [t.id for t in self.trainers]:
            self.trainers.append(trainer)

    def add_equipment(self, equipment):
        if equipment.id not in [e.id for e in self.equipment]:
            self.equipment.append(equipment)

    def add_plan(self, plan):
        if plan.id not in [p.id for p in self.plans]:
            self.plans.append(plan)

    def add_subscription(self, subscription):
        if subscription.id not in [s.id for s in self.subscriptions]:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id):
        subscript = [s for s in self.subscriptions if s.id == subscription_id][0]
        customer_info = [c for c in self.customers if c.id == subscript.customer_id][0]
        trainer_info = [t for t in self.trainers if t.id == subscript.trainer_id][0]
        exercise_info = [e for e in self.plans if e.id == subscript.exercise_id][0]
        equipment_info = [eq for eq in self.equipment if eq.id == exercise_info.equipment_id][0]
        return str(subscript) + "\n" + str(customer_info) + "\n" + str(trainer_info) + "\n" + str(
            equipment_info) + "\n" + str(exercise_info)

