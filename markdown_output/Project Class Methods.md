Collapse All Expand All Members Options: Show All  Members Options: Filtered   
---  
DriveWorks SDK Documentation  |   
---|---  
Project Class Methods   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) : Project Class  
---  
  
Include Inherited Members    
Include Protected Members    


Glossary Item Box

For a list of all members of this type, see [Project members](topic3860.md).

# Public Methods

| Name| Description  
---|---|---  
Public Method| [CreateLiveRule](topic3865.md)| Gets a new LiveRule.   
Public Method| CreateObjRef|  (Inherited from System.MarshalByRefObject)  
Public Method| [CreateRenameProcess](topic3866.md)| Creates a new process capable of swapping out one set of names in all the rules in the project, for another set of names.   
Public Method| [CreateSnapshot](topic3867.md)| Creates a snapshot of the project.   
Public Method| [CreateTransactionFactory](topic3868.md)| Creates a transaction factory which can be used to create transactions for common project modification operations.   
Public Method| [EvaluateRule](topic3869.md)| Overloaded. Evaluates the result of the specified rule formula.   
Public Method| [EvaluateRuleForNamedItem](topic3873.md)| Evaluates the result of the specified rule formula as if it had been applied to a particular named item, if the [RuleTechnology](topic3912.md) property is **ProjectRuleTechnology.Excel** then this is the same as [EvaluateRule(String)](topic3870.md), else if it is [ProjectRuleTechnology.Titan](topic2358.md) then the MyName function is affected.   
Public Method| [EvaluateRules](topic3874.md)| Evaluates the result of the specified rule formulae.   
Public Method| [EvaluateRulesForNamedItem](topic3875.md)| Evaluates the result of the specified rule formulae as if they had been applied to a particular named item, if the [RuleTechnology](topic3912.md) property is **ProjectRuleTechnology.Excel** then this is the same as [EvaluateRule(String)](topic3870.md), else if it is [ProjectRuleTechnology.Titan](topic2358.md) then the MyName function is affected.   
Public Method| GetLifetimeService|  (Inherited from System.MarshalByRefObject)  
Public Method| [GetNamedItem](topic3876.md)| Attempts to find a matching named item in within DriveWorks, for example a calculation cell or variable.   
Public Method| [GetRuleFromNamedItem](topic3877.md)| Gets the rule for a named item within DriveWorks, for example a variable or constant.   
Public Method| [GetService](topic3878.md)| Overloaded. Gets a service from the project.   
Public Method| [GetSuppressionContext](topic3881.md)| Suppresses calculation and returns a disposable suppression context which can be used to resume calculation.   
Public Method| [NamesExist](topic3882.md)| Checks the names to ensure they don't already exist in the design master.   
Public Method| [Save](topic3883.md)| Saves the project.   
Public Method| [SetNamedItemValues](topic3884.md)| Sets the values of the specified named items.   
Public Method| [SetService<T>](topic3885.md)| Sets a service on the Project.   
Public Method| [TryExecuteMacro](topic3886.md)| Executes the named macro and updates any dependencies.   
Public Method| [TryExecuteMacroWithCaller](topic3887.md)| Executes the named macro and updates any dependencies.   
Public Method| [TryExecuteMacroWithCallerAndPosition](topic3888.md)| Executes the named macro and updates any dependencies.   
Top

# Protected Methods

| Name| Description  
---|---|---  
Protected Method| MemberwiseClone| Overloaded. (Inherited from System.MarshalByRefObject)  
Top

# See Also

#### Reference

[Project Class](topic3859.md)   
[DriveWorks Namespace](topic2159.md)


