![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Members Options: Show All  Members Options: Filtered   
---  
DriveWorks SDK Documentation  |   
---|---  
Project Class Members   
See Also Properties Methods Events [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic3859.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) : Project Class  
---  
  
Include Inherited Members    
Include Protected Members  


Glossary Item Box

The following tables list the members exposed by [Project](topic3859.md).

# ![](dotnetimages/collapse.gif)Public Properties

| Name| Description  
---|---|---  
![Public Property](dotnetimages/publicProperty.gif)| [BaseDirectory](topic3889.md)| Gets the base directory which is the project directory for a project, and the specification metadata directory for a specification.   
![Public Property](dotnetimages/publicProperty.gif)| [CalculationTables](topic3890.md)| Gets the object responsible for managing the project's calculation tables.   
![Public Property](dotnetimages/publicProperty.gif)| [ComponentSets](topic3891.md)| Gets the object responsible for managing the project's component sets.   
![Public Property](dotnetimages/publicProperty.gif)| [ComponentTasks](topic3892.md)| Gets the manager for [DriveWorks.Components.Tasks.ComponentTask](topic6407.md)s that are not specific to a single component.   
![Public Property](dotnetimages/publicProperty.gif)| [ConnectionManager](topic3893.md)| Gets the connection manager for the project (and all other projects created by the same engine host).   
![Public Property](dotnetimages/publicProperty.gif)| [ConstantCategories](topic3894.md)| Gets the project's constant categories.   
![Public Property](dotnetimages/publicProperty.gif)| [Constants](topic3895.md)| Gets the object responsible for managing the project's constants.   
![Public Property](dotnetimages/publicProperty.gif)| [DataTables](topic3896.md)| Gets the object responsible for managing the project's data tables.   
![Public Property](dotnetimages/publicProperty.gif)| [Documents](topic3897.md)| Gets the object responsible for managing the project's documents.   
![Public Property](dotnetimages/publicProperty.gif)| [Group](topic3898.md)| Gets the group from which the project was opened.   
![Public Property](dotnetimages/publicProperty.gif)| [Id](topic3899.md)| Gets a GUID which uniquely identifies the project.   
![Public Property](dotnetimages/publicProperty.gif)| [IsClosed](topic3900.md)| Determines whether the project is closed.   
![Public Property](dotnetimages/publicProperty.gif)| [IsOpen](topic3901.md)| Gets whether the project is open or not.   
![Public Property](dotnetimages/publicProperty.gif)| [LocalizationHelper](topic3902.md)| Gets a rule localization helper which is valid for the open project.   
![Public Property](dotnetimages/publicProperty.gif)| [Messages](topic3903.md)| Gets the object responsible for managing the project's messages which are used in form controls to give interactive feedback to users.   
![Public Property](dotnetimages/publicProperty.gif)| [Metadata](topic3904.md)| Gets access to the sections in the project metadata file.   
![Public Property](dotnetimages/publicProperty.gif)| [Name](topic3905.md)| Gets the name of the project.   
![Public Property](dotnetimages/publicProperty.gif)| [Navigation](topic3906.md)| Gets the object responsible for managing the project's form navigation information.   
![Public Property](dotnetimages/publicProperty.gif)| [OriginalVersion](topic3907.md)| Gets the version of the project when it was loaded from file. This is not the current version, as it could have been upgraded since it was loaded.   
![Public Property](dotnetimages/publicProperty.gif)| [Profiler](topic3908.md)| Gets the profiler for the project.   
![Public Property](dotnetimages/publicProperty.gif)| [ProjectFilePath](topic3909.md)| Gets the full path to the project file.   
![Public Property](dotnetimages/publicProperty.gif)| [Properties](topic3910.md)| Gets access to specification properties for the project.   
![Public Property](dotnetimages/publicProperty.gif)| [ReportingLevel](topic3911.md)| Gets the effective reporting level for the project.   
![Public Property](dotnetimages/publicProperty.gif)| [RuleTechnology](topic3912.md)| Gets the rule technology used in this Project.   
![Public Property](dotnetimages/publicProperty.gif)| [SpecialVariables](topic3913.md)| Gets the object responsible for managing the project's special variables.   
![Public Property](dotnetimages/publicProperty.gif)| [SpecificationContext](topic3914.md)| Gets the active specification context if the project has been opened as part of a specification.   
![Public Property](dotnetimages/publicProperty.gif)| [SpecificationFlow](topic3915.md)| Gets the specification-flow which defines the process which is followed for a specification created from this project.   
![Public Property](dotnetimages/publicProperty.gif)| [SpecificationMacroCategories](topic3916.md)| Gets the specification macro categories defined in the project.   
![Public Property](dotnetimages/publicProperty.gif)| [SpecificationMacros](topic3917.md)| Gets the specification macros defined in the project.   
![Public Property](dotnetimages/publicProperty.gif)| [SpecificationSettings](topic3918.md)| Gets access to settings which affect specifications based on the project.   
![Public Property](dotnetimages/publicProperty.gif)| [Utility](topic3919.md)| Gets access to utility methods for the project.   
![Public Property](dotnetimages/publicProperty.gif)| [VariableCategories](topic3920.md)| Gets the project's variable categories.   
![Public Property](dotnetimages/publicProperty.gif)| [Variables](topic3921.md)| Gets the project's variables.   
![Public Property](dotnetimages/publicProperty.gif)| [Version](topic3922.md)| Gets the current version of the project.   
Top

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

# ![](dotnetimages/collapse.gif)Public Events

| Name| Description  
---|---|---  
![Public Event](dotnetimages/publicEvent.gif)| [ExtenderLoadingFailed](topic3923.md)| Raised when one or more project extenders failed to load.   
![Public Event](dotnetimages/publicEvent.gif)| [Saved](topic3924.md)| Raised when the project saves successfully.   
![Public Event](dotnetimages/publicEvent.gif)| [SnapshotCreated](topic3925.md)| Raised when a snapshot of the project is created successfully.   
Top

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[Project Class](topic3859.md)   
[DriveWorks Namespace](topic2159.md)

©2024 DriveWorks Ltd. All Rights Reserved.
