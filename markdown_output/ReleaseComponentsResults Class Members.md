ReleaseComponentsResults Class Members   
See Also Properties Methods [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic6300.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Components Namespace](topic6089.md) : ReleaseComponentsResults Class  
---  
  
Include Inherited Members    
Include Protected Members  


Glossary Item Box

The following tables list the members exposed by [ReleaseComponentsResults](topic6300.md).

# Public Properties

| Name| Description  
---|---|---  
![Public Property](dotnetimages/publicProperty.gif)| [Components](topic6316.md)| Gets all of the components which were released.   
![Public Property](dotnetimages/publicProperty.gif)| [Dependencies](topic6317.md)| Gets the identifiers of all of the driven components on which the specification is dependent.   
![Public Property](dotnetimages/publicProperty.gif)| [DescendantId](topic6318.md)| Gets the identifier of the descendant specification to which the release results belong.   
![Public Property](dotnetimages/publicProperty.gif)| [Flags](topic6319.md)| Gets the flags for all components released within this cycle.   
![Public Property](dotnetimages/publicProperty.gif)| [References](topic6320.md)| Gets all of the component references which were released.   
![Public Property](dotnetimages/publicProperty.gif)| [RootComponents](topic6321.md)| Gets the components that exist at root level.   
![Public Property](dotnetimages/publicProperty.gif)| [ScopedTasks](topic6322.md)| Gets the scoped [DriveWorks.Components.Tasks.ComponentTask](topic6407.md)s that were released.   
![Public Property](dotnetimages/publicProperty.gif)| [SpecificationId](topic6323.md)| Gets the identifier of the specification to which the release results belong.   
Top

# Public Methods

| Name| Description  
---|---|---  
![Public Method](dotnetimages/publicMethod.gif)| [ConvertToReferenceTree](topic6306.md)| Converts the release results to a complete component reference tree by copying across reference information from this release session, and retrieving information for precedent components that were released in other sessions from the group.   
![Public Method](dotnetimages/publicMethod.gif)| [GetComponent](topic6307.md)| Gets a released component based on it's unique identifier.   
![Public Method](dotnetimages/publicMethod.gif)| [GetComponentReferences](topic6308.md)| Gets the references for the component with the specified identifer.   
![Public Method](dotnetimages/publicMethod.gif)| [GetRootComponent](topic6309.md)| Gets a root component based on the name of the component set   
![Public Method](dotnetimages/publicMethod.gif)![static \(Shared in Visual Basic\)](dotnetimages/static.gif)| [Load](topic6310.md)| Overloaded. Loads the released component results from the given XML.   
![Public Method](dotnetimages/publicMethod.gif)| [Save](topic6315.md)| Saves the released component results as an XML document.   
Top

# See Also

#### Reference

[ReleaseComponentsResults Class](topic6300.md)   
[DriveWorks.Components Namespace](topic6089.md)


