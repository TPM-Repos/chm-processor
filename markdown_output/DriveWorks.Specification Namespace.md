Collapse All Expand All  
---  
DriveWorks SDK Documentation  |   
---|---  
DriveWorks.Specification Namespace   
See Also [Inheritance Hierarchy](topic10765.md) [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic10764.md)  
[DriveWorks.Engine Assembly](topic2156.md) : DriveWorks.Specification Namespace  
---  
  
Glossary Item Box

Provides types related to running DriveWorks Projects. 

# Classes

| Class| Description  
---|---|---  
![Class](dotnetimages/Class.gif)| [AdditionalFoldersCreatedEventArgs](topic10775.md) | Provides the event data for the additional folder creation event.  
![Class](dotnetimages/Class.gif)| [AvailableOperation](topic10787.md) | Provides information about the runtime availability of an operation.  
![Class](dotnetimages/Class.gif)| [AvailableTransition](topic10796.md) | Provides information about the runtime availability of a transition.  
![Class](dotnetimages/Class.gif)| [Condition](topic10804.md) | Represents a condition which governs the availability of an operation, task, or transition in a specification-flow.  
![Class](dotnetimages/Class.gif)| [ConditionAttribute](topic10832.md) | Provides descriptive information about a condition.  
![Class](dotnetimages/Class.gif)| [ConditionEventArgs](topic10843.md) | Provides the event data for condition events.  
![Class](dotnetimages/Class.gif)| [ConditionNotFoundException](topic10854.md) | Thrown when a project cannot be loaded because implementations could not be found for one or more conditions.  
![Class](dotnetimages/Class.gif)| [Conditions](topic10865.md) | Manages the conditions which govern the availability of an item in a specification-flow.  
![Class](dotnetimages/Class.gif)| [EventSequenceEventArgs](topic10886.md) | Provides the event data for event events.  
![Class](dotnetimages/Class.gif)| [FlowEvent](topic10897.md) | Represents an event in a specification-flow.  
![Class](dotnetimages/Class.gif)| [FlowProperties](topic10905.md) | Represents a collection of specification-flow properties.  
![Class](dotnetimages/Class.gif)| [FlowProperty](topic10946.md) | Represents an untyped property on a condition or task.  
![Class](dotnetimages/Class.gif)| [FlowProperty<T>](topic10978.md) | Represents a typed property on a condition or task.  
![Class](dotnetimages/Class.gif)| [FlowPropertyInfo](topic10992.md) | Provides descriptive information about a flow property.  
![Class](dotnetimages/Class.gif)| [IncompleteNavigationException](topic11007.md) | Thrown when a specification is started based on a project with an incomplete navigation.  
![Class](dotnetimages/Class.gif)| [InitialStateInvalidException](topic11018.md) | Thrown when a specification cannot be loaded because the initial state is not specified.  
![Class](dotnetimages/Class.gif)| [InvalidTransitionTargetException](topic11027.md) | Thrown when a specficaiton transition has no target state or connects two running states together.  
![Class](dotnetimages/Class.gif)| [MacroAbortedException](topic11038.md) | Thrown when DriveWorks macro execution is aborted.  
![Class](dotnetimages/Class.gif)| [NoInitialStateException](topic11048.md) | Thrown when an attempt is made to start a specification based on a project with a specification flow whose initial state is not set.  
![Class](dotnetimages/Class.gif)| [NotRunningStateException](topic11058.md) | Thrown when an attempt is made to start a specification based on a project with a specification flow whose initial state is not a running state.  
![Class](dotnetimages/Class.gif)| [Operation](topic11068.md) | Represents an operation which can be invoked for a given state.  
![Class](dotnetimages/Class.gif)| [OperationEventArgs](topic11084.md) | Provides the event data for operation events.  
![Class](dotnetimages/Class.gif)| [Operations](topic11095.md) | Manages the operations which are available for a given state in a specification-flow.  
![Class](dotnetimages/Class.gif)| [ProjectDetailsEventArgs](topic11112.md) | Provides the event data for project details events.  
![Class](dotnetimages/Class.gif)| [PropertyInvalidException](topic11123.md) | Thrown when a project cannot be loaded because a referenced property could not be found or was of the wrong type.  
![Class](dotnetimages/Class.gif)| [RuleResults](topic11136.md) | Provides access to the rule results for an entity such as a document or component.  
![Class](dotnetimages/Class.gif)| [SpecificationContext](topic11149.md) | Provides contextual information to a running specification-flow.  
![Class](dotnetimages/Class.gif)| [SpecificationContextEventArgs](topic11284.md) | Provides event data for events involving a specification context.  
![Class](dotnetimages/Class.gif)| [SpecificationDetails](topic11292.md) | Provides information about a registered DriveWorks specification.  
![Class](dotnetimages/Class.gif)| [SpecificationDetailsEventArgs](topic11322.md) | Provides the event data for specification details events.  
![Class](dotnetimages/Class.gif)| [SpecificationDocumentDetails](topic11333.md) | Provides information about a registered specification document.  
![Class](dotnetimages/Class.gif)| [SpecificationDocumentEventArgs](topic11344.md) | Provides the event data for specification document events.  
![Class](dotnetimages/Class.gif)| [SpecificationEnvironment](topic11355.md) | Provides the environment required for a specification.  
![Class](dotnetimages/Class.gif)| [SpecificationExistsException](topic11376.md) | Thrown when a transition could not be invoked because a specification with the same name already exists.  
![Class](dotnetimages/Class.gif)| [SpecificationFlowDefinition](topic11387.md) | Supports working with a customized specification-flow definition on a project.  
![Class](dotnetimages/Class.gif)| [SpecificationForm](topic11402.md) | Provides information about a form in the navigation of a running specification.  
![Class](dotnetimages/Class.gif)| [SpecificationHostControlContextEventArgs](topic11418.md) | Provides event data for Specification host control based events on specification contexts.  
![Class](dotnetimages/Class.gif)| [SpecificationMacro](topic11429.md) | Represents a specification macro.  
![Class](dotnetimages/Class.gif)| [SpecificationMacroEventArgs](topic11456.md) | Provides the event data for specification macro events.  
![Class](dotnetimages/Class.gif)| [SpecificationMacros](topic11467.md) | Provides access to the specification macros in a project.  
![Class](dotnetimages/Class.gif)| [SpecificationNameInvalidException](topic11488.md) | Thrown when a transition could not be invoked because the specification name is invalid.  
![Class](dotnetimages/Class.gif)| [SpecificationNameRuleInvalidException](topic11499.md) | Thrown when a transition could not be invoked because the specification's name rule is invalid.  
![Class](dotnetimages/Class.gif)| [SpecificationTaskDetails](topic11510.md) | Provides information about a registered DriveWorks specification task.  
![Class](dotnetimages/Class.gif)| [SpecificationTaskList](topic11525.md) | Encapsulates the task list for a running specification.  
![Class](dotnetimages/Class.gif)| [SpecificationTaskListEntry](topic11537.md) | Represents an entry in a running specification's task list.  
![Class](dotnetimages/Class.gif)| [SpecificationTaskListEntryEventArgs](topic11548.md) | Provides event data for specification task list entry events.  
![Class](dotnetimages/Class.gif)| [State](topic11559.md) | Provides a means for working with the definition of a specific state in a specification-flow.  
![Class](dotnetimages/Class.gif)| [StateChangeEventArgs](topic11578.md) | Provides the event data for state change events.  
![Class](dotnetimages/Class.gif)| [StateEventArgs](topic11590.md) | Provides the event data for state events.  
![Class](dotnetimages/Class.gif)| [StateNotFoundException](topic11601.md) | Thrown when a project cannot be loaded because one or more referenced states could not be found.  
![Class](dotnetimages/Class.gif)| [States](topic11612.md) | Provides access to the states for a specification flow.  
![Class](dotnetimages/Class.gif)| [Task](topic11629.md) | The base class for all tasks which can be added to the task sequences for events which get fired by operations, transitions, and states.  
![Class](dotnetimages/Class.gif)| [TaskAttribute](topic11659.md) | Provides descriptive information about a task.  
![Class](dotnetimages/Class.gif)| [TaskEventArgs](topic11672.md) | Provides the event data for task events.  
![Class](dotnetimages/Class.gif)| [TaskExecutionException](topic11683.md) | Thrown when a DriveWorks task fails to run.  
![Class](dotnetimages/Class.gif)| [TaskListNotEmptyException](topic11691.md) | Thrown when the task list contains tasks which require resolution before performing some action in the specification.  
![Class](dotnetimages/Class.gif)| [TaskNotFoundException](topic11702.md) | Thrown when a project cannot be loaded because implementations could not be found for one or more tasks.  
![Class](dotnetimages/Class.gif)| [TaskSequence](topic11713.md) | Represents a sequence of tasks to be executed for an operation or event.  
![Class](dotnetimages/Class.gif)| [Teams](topic11737.md) | Manages the list of teams which have access to a given item in a specification-flow.  
![Class](dotnetimages/Class.gif)| [Transition](topic11757.md) | Represents a transition from one state to another.  
![Class](dotnetimages/Class.gif)| [TransitionEventArgs](topic11776.md) | Provides the event data for transition events.  
![Class](dotnetimages/Class.gif)| [Transitions](topic11787.md) | Manages the transitions which are available for a given state in a specification-flow.  
![Class](dotnetimages/Class.gif)| [UnparsableFlowPropertyValueException](topic11805.md) | Thrown when a FlowProperty's rule results in a value that can't be parsed to the FlowProperty's type.  
  
# Delegates

| Delegate| Description  
---|---|---  
![Delegate](dotnetimages/Delegate.gif)| [AdditionalFoldersCreatedEventHandler](topic11817.md) | Represents a method which will handle the creation of additional folders.  
![Delegate](dotnetimages/Delegate.gif)| [ConditionEventHandler](topic11818.md) | Represents a method which will handle a condition event.  
![Delegate](dotnetimages/Delegate.gif)| [EventSequenceEventHandler](topic11819.md) | Represents a method which will handle an event sequence event.  
![Delegate](dotnetimages/Delegate.gif)| [OperationEventHandler](topic11820.md) | Represents a method which will handle an operation event.  
![Delegate](dotnetimages/Delegate.gif)| [SpecificationContextEventHandler](topic11821.md) | Represents a method that will handle events involving specification context.  
![Delegate](dotnetimages/Delegate.gif)| [SpecificationDocumentEventHandler](topic11822.md) | Represents a method which will handle a specification document event.  
![Delegate](dotnetimages/Delegate.gif)| [SpecificationTaskListEntryEventHandler](topic11823.md) | Represents a method that will handle events related to specification task list entries.  
![Delegate](dotnetimages/Delegate.gif)| [StateChangeEventHandler](topic11824.md) | Represents a method which will handle a state change event.  
![Delegate](dotnetimages/Delegate.gif)| [StateEventHandler](topic11825.md) | Represents a method which will handle a state event.  
![Delegate](dotnetimages/Delegate.gif)| [TaskEventHandler](topic11826.md) | Represents a method which will handle a task event.  
![Delegate](dotnetimages/Delegate.gif)| [TransitionEventHandler](topic11827.md) | Represents a method which will handle a transition event.  
  
# Enumerations

| Enumeration| Description  
---|---|---  
![Enumeration](dotnetimages/Enumeration.gif)| [ConditionFailBehavior](topic10766.md) | Specifies the behavior of an item to which a condition is attached when the condition evaluates to false.  
![Enumeration](dotnetimages/Enumeration.gif)| [ConditionResult](topic10767.md) | Specifies the result of evaluating a condition.  
![Enumeration](dotnetimages/Enumeration.gif)| [DocumentGenerationOptions](topic10768.md) | Provides possible values for the document generation setting which governs when documents get generated using the default specification-flow.  
![Enumeration](dotnetimages/Enumeration.gif)| [MacroConsistencyLevel](topic10769.md) | Determines the required consistency level of the macro.  
![Enumeration](dotnetimages/Enumeration.gif)| [NavigationOptions](topic10770.md) | The options available for navigation.  
![Enumeration](dotnetimages/Enumeration.gif)| [SpecificationDialogCloseOptions](topic10771.md) | Value used by [SpecificationForm](topic11402.md) to depict it's available closing options.  
![Enumeration](dotnetimages/Enumeration.gif)| [SpecificationType](topic10772.md) | Represents the type of a specification, i.e. whether it was newly created, copied, etc.  
![Enumeration](dotnetimages/Enumeration.gif)| [StateType](topic10773.md) | Represents the type of state.  
![Enumeration](dotnetimages/Enumeration.gif)| [TaskListEntryType](topic10774.md) | The type of a task list entry.  
  
# See Also

#### Reference

[DriveWorks.Engine Assembly](topic2156.md)


