#!/usr/bin/env python3
import aws_cdk as cdk
from infraestrutura.infraestrutura_stack import InfraestruturaStack

app = cdk.App()
InfraestruturaStack(app, "InfraestruturaStack")
app.synth()
