![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Members Options: Show All  Members Options: Filtered   
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

# ![](dotnetimages/collapse.gif)Public Methods

| Name| Description  
---|---|---  
![Public Method](dotnetimages/publicMethod.gif)| CreateObjRef|  (Inherited from System.MarshalByRefObject)  
![Public Method](dotnetimages/publicMethod.gif)| [CreateReportWriter](topic3244.md)| Creates a new report writer which will write a report for the given component.   
![Public Method](dotnetimages/publicMethod.gif)| [DeleteFileReferenceByTargetPath](topic3245.md)| Deletes a released component and references to it from the group.   
![Public Method](dotnetimages/publicMethod.gif)| [DeleteReleasedComponentReport](topic3246.md)| Deletes the specified component report.   
![Public Method](dotnetimages/publicMethod.gif)| [DeleteReleasedComponentReports](topic3247.md)| Deletes all component reports for the specified component.   
![Public Method](dotnetimages/publicMethod.gif)| [GetComponent](topic3248.md)| Gets the released component with the specified identifier.   
![Public Method](dotnetimages/publicMethod.gif)| [GetComponentDetailsById](topic3249.md)| Get's the component details for a component with the specified identifier.   
![Public Method](dotnetimages/publicMethod.gif)| [GetComponentDetailsByName](topic3250.md)| Get's the component details for a component with the specified name.   
![Public Method](dotnetimages/publicMethod.gif)| [GetComponentDetailsByPath](topic3251.md)| Get's the component details for a component with the specified path.   
![Public Method](dotnetimages/publicMethod.gif)| [GetComponentReferences](topic3252.md)| Gets an object which will enumerate the released component references in the group.   
![Public Method](dotnetimages/publicMethod.gif)| [GetComponentReferenceTree](topic3253.md)| Gets hierarchical reference information about the components with the given identifiers.   
![Public Method](dotnetimages/publicMethod.gif)| [GetComponents](topic3254.md)| Overloaded. Gets an object which will enumerate the released components in the group.   
![Public Method](dotnetimages/publicMethod.gif)| [GetComponentsAwaitingPreviewEnumerator](topic3257.md)| Gets an object which will enumerate the released components that are awaiting a preview in the group.   
![Public Method](dotnetimages/publicMethod.gif)| [GetComponentsDetailsById](topic3258.md)| Gets the details of all driven components matching the specified component ids.   
![Public Method](dotnetimages/publicMethod.gif)| [GetComponentsForGenerationInSpecificationOrder](topic3259.md)| Internal Use Only. Gets components which are generatable (i.e. they have no ungenerated children), in the order of the specifications to which they belong.   
![Public Method](dotnetimages/publicMethod.gif)| GetLifetimeService|  (Inherited from System.MarshalByRefObject)  
![Public Method](dotnetimages/publicMethod.gif)| [GetOrphanComponentsForGeneration](topic3260.md)| Internal Use Only. Gets components which are generatable (i.e. they have no ungenerated children), and which don't belong to any specifications.   
![Public Method](dotnetimages/publicMethod.gif)| [GetReports](topic3261.md)| Gets a specification's reports.   
![Public Method](dotnetimages/publicMethod.gif)| [MarkFailed](topic3262.md)| Marks the specified component as having failed the given number of times.   
![Public Method](dotnetimages/publicMethod.gif)| [MarkGenerated](topic3263.md)| Marks the specified component as being generated.   
![Public Method](dotnetimages/publicMethod.gif)| [MarkGenerating](topic3264.md)| Marks the specified component as being in the process of being generated.   
![Public Method](dotnetimages/publicMethod.gif)| [MarkToGenerate](topic3265.md)| Marks the specified component as requiring generation.   
![Public Method](dotnetimages/publicMethod.gif)| [SaveReleaseResults](topic3266.md)| Saves the results of releasing one or more components.   
![Public Method](dotnetimages/publicMethod.gif)| [TryUpdateMasterPath](topic3267.md)| Tries to update the master path of all released components matching the specified master path.   
![Public Method](dotnetimages/publicMethod.gif)| [TryUpdatePreviewPath](topic3268.md)| Updates the path to the preview file created for the specified component.   
![Public Method](dotnetimages/publicMethod.gif)| [TryUpdateTargetPath](topic3269.md)| Tries to update the target path of a released component.   
![Public Method](dotnetimages/publicMethod.gif)| [UpdateReleasedComponentFlags](topic3270.md)| Updates the specified released component's flags.   
![Public Method](dotnetimages/publicMethod.gif)| [UpdateReleasedComponentTags](topic3271.md)| Updates the specified released component's tags.   
Top

# ![](dotnetimages/collapse.gif)Protected Methods

| Name| Description  
---|---|---  
![Protected Method](dotnetimages/protectedMethod.gif)| MemberwiseClone| Overloaded. (Inherited from System.MarshalByRefObject)  
Top

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[GroupReleasedComponents Class](topic3238.md)   
[DriveWorks Namespace](topic2159.md)

©2024 DriveWorks Ltd. All Rights Reserved.
