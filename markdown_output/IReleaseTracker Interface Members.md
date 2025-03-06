![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Members Options: Show All  Members Options: Filtered   
---  
DriveWorks SDK Documentation  |   
---|---  
IReleaseTracker Interface Members   
See Also Methods [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic6119.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Components Namespace](topic6089.md) : IReleaseTracker Interface  
---  
  
Include Inherited Members    


Glossary Item Box

The following tables list the members exposed by [IReleaseTracker](topic6119.md).

# ![](dotnetimages/collapse.gif)Public Methods

| Name| Description  
---|---|---  
![ Method](dotnetimages/Method.gif)| [Finish](topic6124.md)| Informs the trackers that the release process has finished.   
![ Method](dotnetimages/Method.gif)| [NotifyBeginEvaluate](topic6125.md)| Called when the evaluation of a component has begun.   
![ Method](dotnetimages/Method.gif)| [NotifyBeginRelease](topic6126.md)| Called when the release of an evaluated component has started.   
![ Method](dotnetimages/Method.gif)| [NotifyComponentSetAccepted](topic6127.md)| Called when a component set has its rule evaluated as "delete".   
![ Method](dotnetimages/Method.gif)| [NotifyComponentSetDeleted](topic6128.md)| Called when a component set has its rule evaluated as "delete".   
![ Method](dotnetimages/Method.gif)| [NotifyComponentSetLoadFailed](topic6129.md)| Called when a component set's root compoent could not be loaded.   
![ Method](dotnetimages/Method.gif)| [NotifyComponentSetSuppressed](topic6130.md)| Called when a component set has its rule evaluated as "suppress".   
![ Method](dotnetimages/Method.gif)| [NotifyEndEvaluate](topic6131.md)| Called when the evaluation of the current component has ended.   
![ Method](dotnetimages/Method.gif)| [NotifyEndRelease](topic6132.md)| Called when the release of the current component has ended.   
![ Method](dotnetimages/Method.gif)| [NotifyEvaluatedAsAction](topic6133.md)| Called when the current component is determined to need a non-replacement action applying.   
![ Method](dotnetimages/Method.gif)| [NotifyEvaluatedAsDrivenAlternative](topic6134.md)| Called when the current component is determined to need swapping for a driven alternative.   
![ Method](dotnetimages/Method.gif)| [NotifyEvaluatedAsDuplicatePath](topic6135.md)| Called when the current component is determined to have the same path as an existing component, but a different target name.   
![ Method](dotnetimages/Method.gif)| [NotifyEvaluatedAsExistingComponent](topic6136.md)| Called when the current component is determined to have already been evaluated.   
![ Method](dotnetimages/Method.gif)| [NotifyEvaluatedAsInvalidName](topic6137.md)| Called when the current component is determined to have an invalid name.   
![ Method](dotnetimages/Method.gif)| [NotifyEvaluatedAsNewComponent](topic6138.md)| Called when the current component is determined to be a new component.   
![ Method](dotnetimages/Method.gif)| [NotifyEvaluatedAsNewComponentWithInvalidPath](topic6139.md)| Called when the current component is determined to have an invalid full path.   
![ Method](dotnetimages/Method.gif)| [NotifyEvaluatedAsStandardAlternative](topic6140.md)| Called when the current component is determined to need swapping for a standard alternative.   
![ Method](dotnetimages/Method.gif)| [NotifyEvaluatedAsStandardAlternativeWithInvalidPath](topic6141.md)| Called when the current component is determined to need swapping for a standard alternative that has an invalid full path.   
![ Method](dotnetimages/Method.gif)| [NotifyInReleaseComponentParameterResult](topic6142.md)| Called when a parameter result is finalized.   
![ Method](dotnetimages/Method.gif)| [NotifyTrackingIdChanged](topic6143.md)| Called when the current component is going to be used to overwriting an existing component and so the tracking id needs to be changed   
Top

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[IReleaseTracker Interface](topic6119.md)   
[DriveWorks.Components Namespace](topic6089.md)

©2024 DriveWorks Ltd. All Rights Reserved.
