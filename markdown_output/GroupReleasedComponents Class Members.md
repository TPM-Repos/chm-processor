Collapse All Expand All Members Options: Show All  Members Options: Filtered   
---  
DriveWorks SDK Documentation  |   
---|---  
GroupReleasedComponents Class Members   
See Also Methods [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic3238.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) : GroupReleasedComponents Class  
---  
  
Include Inherited Members    
Include Protected Members  


Glossary Item Box

The following tables list the members exposed by [GroupReleasedComponents](topic3238.md).

# Public Methods

| Name| Description  
---|---|---  
Public Method| CreateObjRef|  (Inherited from System.MarshalByRefObject)  
Public Method| [CreateReportWriter](topic3244.md)| Creates a new report writer which will write a report for the given component.   
Public Method| [DeleteFileReferenceByTargetPath](topic3245.md)| Deletes a released component and references to it from the group.   
Public Method| [DeleteReleasedComponentReport](topic3246.md)| Deletes the specified component report.   
Public Method| [DeleteReleasedComponentReports](topic3247.md)| Deletes all component reports for the specified component.   
Public Method| [GetComponent](topic3248.md)| Gets the released component with the specified identifier.   
Public Method| [GetComponentDetailsById](topic3249.md)| Get's the component details for a component with the specified identifier.   
Public Method| [GetComponentDetailsByName](topic3250.md)| Get's the component details for a component with the specified name.   
Public Method| [GetComponentDetailsByPath](topic3251.md)| Get's the component details for a component with the specified path.   
Public Method| [GetComponentReferences](topic3252.md)| Gets an object which will enumerate the released component references in the group.   
Public Method| [GetComponentReferenceTree](topic3253.md)| Gets hierarchical reference information about the components with the given identifiers.   
Public Method| [GetComponents](topic3254.md)| Overloaded. Gets an object which will enumerate the released components in the group.   
Public Method| [GetComponentsAwaitingPreviewEnumerator](topic3257.md)| Gets an object which will enumerate the released components that are awaiting a preview in the group.   
Public Method| [GetComponentsDetailsById](topic3258.md)| Gets the details of all driven components matching the specified component ids.   
Public Method| [GetComponentsForGenerationInSpecificationOrder](topic3259.md)| Internal Use Only. Gets components which are generatable (i.e. they have no ungenerated children), in the order of the specifications to which they belong.   
Public Method| GetLifetimeService|  (Inherited from System.MarshalByRefObject)  
Public Method| [GetOrphanComponentsForGeneration](topic3260.md)| Internal Use Only. Gets components which are generatable (i.e. they have no ungenerated children), and which don't belong to any specifications.   
Public Method| [GetReports](topic3261.md)| Gets a specification's reports.   
Public Method| [MarkFailed](topic3262.md)| Marks the specified component as having failed the given number of times.   
Public Method| [MarkGenerated](topic3263.md)| Marks the specified component as being generated.   
Public Method| [MarkGenerating](topic3264.md)| Marks the specified component as being in the process of being generated.   
Public Method| [MarkToGenerate](topic3265.md)| Marks the specified component as requiring generation.   
Public Method| [SaveReleaseResults](topic3266.md)| Saves the results of releasing one or more components.   
Public Method| [TryUpdateMasterPath](topic3267.md)| Tries to update the master path of all released components matching the specified master path.   
Public Method| [TryUpdatePreviewPath](topic3268.md)| Updates the path to the preview file created for the specified component.   
Public Method| [TryUpdateTargetPath](topic3269.md)| Tries to update the target path of a released component.   
Public Method| [UpdateReleasedComponentFlags](topic3270.md)| Updates the specified released component's flags.   
Public Method| [UpdateReleasedComponentTags](topic3271.md)| Updates the specified released component's tags.   
Top

# Protected Methods

| Name| Description  
---|---|---  
Protected Method| MemberwiseClone| Overloaded. (Inherited from System.MarshalByRefObject)  
Top

# See Also

#### Reference

[GroupReleasedComponents Class](topic3238.md)   
[DriveWorks Namespace](topic2159.md)


