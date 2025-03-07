Collapse All Expand All  
---  
DriveWorks SDK Documentation  |   
---|---  
DriveWorks.Components Namespace   
See Also [Inheritance Hierarchy](topic6090.md) [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic6089.md)  
[DriveWorks.Engine Assembly](topic2156.md) : DriveWorks.Components Namespace  
---  
  
Glossary Item Box

Provides the basis for captured, project, and released components in DriveWorks. 

# Classes

| Class| Description  
---|---|---  
![Class](dotnetimages/Class.gif)| [CapturedComponent](topic6147.md) | Provides the base class for captured components, which should be implemented by a component provider.  
![Class](dotnetimages/Class.gif)| [CapturedComponentInfo](topic6154.md) | Provides information about a captured component.  
![Class](dotnetimages/Class.gif)| [ComponentFactoryAttribute](topic6167.md) | Used to indicate to DriveWorks the factory that is responsible for creating components of a given type.  
![Class](dotnetimages/Class.gif)| [MissingProjectComponent](topic6175.md) | Provides a project component implementation for project components whose underlying capture data can't be resolved.  
![Class](dotnetimages/Class.gif)| [ProjectComponent](topic6183.md) | Provides the base class for project components, which should be implemented by a component provider.  
![Class](dotnetimages/Class.gif)| [ProjectComponentRule](topic6198.md) | Represents a rule on a project component or parameter.  
![Class](dotnetimages/Class.gif)| [ProjectComponentRuleProxy](topic6216.md) | Provides a base for inheriting from ProjectComponentRule.  
![Class](dotnetimages/Class.gif)| [ProjectComponents](topic6229.md) | Provides a collection of project components.  
![Class](dotnetimages/Class.gif)| [ReadOnlyReleasedComponentReferenceDetails](topic6239.md) | Provides a read-only wrapper around an instance of the [ReleasedComponentReferenceDetails](topic6356.md) class.  
![Class](dotnetimages/Class.gif)| [ReleaseComponentController](topic6252.md) | Provided to a component during its release to give it the opportunity to control certain aspects of its release process.  
![Class](dotnetimages/Class.gif)| [ReleaseComponentHelper](topic6275.md) | Implements the release process for components.  
![Class](dotnetimages/Class.gif)| [ReleaseComponentReportTracker](topic6292.md) | Create a tracker to report on the release process of a component.  
![Class](dotnetimages/Class.gif)| [ReleaseComponentsResults](topic6300.md) | Encapsulates the results of releasing one or more component sets.  
![Class](dotnetimages/Class.gif)| [ReleasedComponent](topic6324.md) | Provides the base class for drive components, which should be implemented by a component provider.  
![Class](dotnetimages/Class.gif)| [ReleasedComponentDetails](topic6336.md) | Provides information about a released component.  
![Class](dotnetimages/Class.gif)| [ReleasedComponentReferenceDetails](topic6356.md) | Provides information about a reference from one driven component to another.  
![Class](dotnetimages/Class.gif)| [ReleasedComponentTaskCondition](topic6370.md) | Represents a released [DriveWorks.Components.Tasks.ComponentTaskCondition](topic6493.md).  
![Class](dotnetimages/Class.gif)| [ReleaseEnvironment](topic6379.md) | Provides the environment required for releasing one or more components.  
  
# Interfaces

| Interface| Description  
---|---|---  
![Interface](dotnetimages/Interface.gif)| [IComponentFactory](topic6091.md) | Provides a means for dynamically constructing components of a certain type.  
![Interface](dotnetimages/Interface.gif)| [IHasReferences](topic6099.md) | provides a contract for an object that has external file references associated with it.  
![Interface](dotnetimages/Interface.gif)| [IReleasedComponentReferenceTree](topic6106.md) | Provides information about one or more released components and their relationships.  
![Interface](dotnetimages/Interface.gif)| [IReleaseParameterTracker](topic6113.md) | Provides support for a component being released to provide diagnosting information about a parameter which was released.  
![Interface](dotnetimages/Interface.gif)| [IReleaseTracker](topic6119.md) | Provides a contract for an object which is used to track the release of components.  
  
# Enumerations

| Enumeration| Description  
---|---|---  
![Enumeration](dotnetimages/Enumeration.gif)| [ComponentReferenceType](topic6144.md) | Specifies whether a component is a standard or a derived component.  
![Enumeration](dotnetimages/Enumeration.gif)| [ReleasedComponentFlags](topic6145.md) | Specifies additional behaviour for [ReleasedComponent](topic6324.md)s.  
![Enumeration](dotnetimages/Enumeration.gif)| [ReleasedComponentReferenceAction](topic6146.md) | Specifies the action to take for a released component reference.  
  
# See Also

#### Reference

[DriveWorks.Engine Assembly](topic2156.md)


