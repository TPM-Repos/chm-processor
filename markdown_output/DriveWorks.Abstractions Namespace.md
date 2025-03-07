Collapse All Expand All  
---  
DriveWorks SDK Documentation  |   
---|---  
DriveWorks.Abstractions Namespace   
See Also [Inheritance Hierarchy](topic5940.md) [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic5939.md)  
[DriveWorks.Engine Assembly](topic2156.md) : DriveWorks.Abstractions Namespace  
---  
  
Glossary Item Box

Provides types which provide abstractions which are common in the DriveWorks Engine such as common interfaces implemented by rules bound objects. 

# Classes

| Class| Description  
---|---|---  
![Class](dotnetimages/Class.gif)| [AliasRule](topic6001.md) | Provides a [IHasRule](topic5947.md) implementation which acts as an alias for another [IHasRule](topic5947.md).  
![Class](dotnetimages/Class.gif)| [BufferedRule](topic6017.md) | Provides an implementation of the [IHasRule](topic5947.md) implementation which acts as a buffer between a rule, and a rule consumer.  
![Class](dotnetimages/Class.gif)| [BufferedRuleWithVersionHistory](topic6035.md) | Provides an implementation of the [IHasRule](topic5947.md) implementation which acts as a buffer between a rule, and a rule consumer.  
![Class](dotnetimages/Class.gif)| [GenericRule](topic6043.md) | Provides a simple implementation of the [IHasRule](topic5947.md) implementation.  
![Class](dotnetimages/Class.gif)| [GenericRuleWithCustomName](topic6063.md) | Provides a simple implementation of the [IHasRule](topic5947.md) implementation with customized support for the MyName function.  
![Class](dotnetimages/Class.gif)| [Lock](topic6079.md) | Provides an object which can be used to help implement the [ILockable](topic5981.md) interface.  
  
# Interfaces

| Interface| Description  
---|---|---  
![Interface](dotnetimages/Interface.gif)| [ICustomizable](topic5941.md) | Represents an object which supports customization.  
![Interface](dotnetimages/Interface.gif)| [IHasRule](topic5947.md) | Provides a contract for items which have a rule.  
![Interface](dotnetimages/Interface.gif)| [IHasRuleId](topic5957.md) | Implemented by rules which have invariant identifiers.  
![Interface](dotnetimages/Interface.gif)| [IHasRuleName](topic5963.md) | Implemented by items which have names which can be referenced in rules.  
![Interface](dotnetimages/Interface.gif)| [IHasRuleType](topic5969.md) | Provides a contract for items which have a rule which is typed.  
![Interface](dotnetimages/Interface.gif)| [IHasRuleVersionHistory](topic5975.md) | Provides a contract for items which have a rule version history.  
![Interface](dotnetimages/Interface.gif)| [ILockable](topic5981.md) | Provides a contract for objects which can be locked to prevent modification.  
![Interface](dotnetimages/Interface.gif)| [INotifyRuleChanged](topic5987.md) | Provides a contract for an object to notify when its rule changes.  
![Interface](dotnetimages/Interface.gif)| [IResourceUrlProvider](topic5993.md) | Provides a contract for retrieving URLs for resources.  
  
# See Also

#### Reference

[DriveWorks.Engine Assembly](topic2156.md)


