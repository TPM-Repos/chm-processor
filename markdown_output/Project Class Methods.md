![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Members Options: Show All  Members Options: Filtered   
---  
DriveWorks SDK Documentation  |   
---|---  
Project Class Methods   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic3859.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) : Project Class  
---  
  
Include Inherited Members    
Include Protected Members    


Glossary Item Box

For a list of all members of this type, see [Project members](topic3860.md).

# ![](dotnetimages/collapse.gif)Public Methods

| Name| Description  
---|---|---  
![Public Method](dotnetimages/publicMethod.gif)| [CreateLiveRule](topic3865.md)| Gets a new LiveRule.   
![Public Method](dotnetimages/publicMethod.gif)| CreateObjRef|  (Inherited from System.MarshalByRefObject)  
![Public Method](dotnetimages/publicMethod.gif)| [CreateRenameProcess](topic3866.md)| Creates a new process capable of swapping out one set of names in all the rules in the project, for another set of names.   
![Public Method](dotnetimages/publicMethod.gif)| [CreateSnapshot](topic3867.md)| Creates a snapshot of the project.   
![Public Method](dotnetimages/publicMethod.gif)| [CreateTransactionFactory](topic3868.md)| Creates a transaction factory which can be used to create transactions for common project modification operations.   
![Public Method](dotnetimages/publicMethod.gif)| [EvaluateRule](topic3869.md)| Overloaded. Evaluates the result of the specified rule formula.   
![Public Method](dotnetimages/publicMethod.gif)| [EvaluateRuleForNamedItem](topic3873.md)| Evaluates the result of the specified rule formula as if it had been applied to a particular named item, if the [RuleTechnology](topic3912.md) property is **ProjectRuleTechnology.Excel** then this is the same as [EvaluateRule(String)](topic3870.md), else if it is [ProjectRuleTechnology.Titan](topic2358.md) then the MyName function is affected.   
![Public Method](dotnetimages/publicMethod.gif)| [EvaluateRules](topic3874.md)| Evaluates the result of the specified rule formulae.   
![Public Method](dotnetimages/publicMethod.gif)| [EvaluateRulesForNamedItem](topic3875.md)| Evaluates the result of the specified rule formulae as if they had been applied to a particular named item, if the [RuleTechnology](topic3912.md) property is **ProjectRuleTechnology.Excel** then this is the same as [EvaluateRule(String)](topic3870.md), else if it is [ProjectRuleTechnology.Titan](topic2358.md) then the MyName function is affected.   
![Public Method](dotnetimages/publicMethod.gif)| GetLifetimeService|  (Inherited from System.MarshalByRefObject)  
![Public Method](dotnetimages/publicMethod.gif)| [GetNamedItem](topic3876.md)| Attempts to find a matching named item in within DriveWorks, for example a calculation cell or variable.   
![Public Method](dotnetimages/publicMethod.gif)| [GetRuleFromNamedItem](topic3877.md)| Gets the rule for a named item within DriveWorks, for example a variable or constant.   
![Public Method](dotnetimages/publicMethod.gif)| [GetService](topic3878.md)| Overloaded. Gets a service from the project.   
![Public Method](dotnetimages/publicMethod.gif)| [GetSuppressionContext](topic3881.md)| Suppresses calculation and returns a disposable suppression context which can be used to resume calculation.   
![Public Method](dotnetimages/publicMethod.gif)| [NamesExist](topic3882.md)| Checks the names to ensure they don't already exist in the design master.   
![Public Method](dotnetimages/publicMethod.gif)| [Save](topic3883.md)| Saves the project.   
![Public Method](dotnetimages/publicMethod.gif)| [SetNamedItemValues](topic3884.md)| Sets the values of the specified named items.   
![Public Method](dotnetimages/publicMethod.gif)| [SetService<T>](topic3885.md)| Sets a service on the Project.   
![Public Method](dotnetimages/publicMethod.gif)| [TryExecuteMacro](topic3886.md)| Executes the named macro and updates any dependencies.   
![Public Method](dotnetimages/publicMethod.gif)| [TryExecuteMacroWithCaller](topic3887.md)| Executes the named macro and updates any dependencies.   
![Public Method](dotnetimages/publicMethod.gif)| [TryExecuteMacroWithCallerAndPosition](topic3888.md)| Executes the named macro and updates any dependencies.   
Top

# ![](dotnetimages/collapse.gif)Protected Methods

| Name| Description  
---|---|---  
![Protected Method](dotnetimages/protectedMethod.gif)| MemberwiseClone| Overloaded. (Inherited from System.MarshalByRefObject)  
Top

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[Project Class](topic3859.md)   
[DriveWorks Namespace](topic2159.md)

©2024 DriveWorks Ltd. All Rights Reserved.
