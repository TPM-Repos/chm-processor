![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Members Options: Show All  Members Options: Filtered   
---  
DriveWorks SDK Documentation  |   
---|---  
ProjectPart Class Members   
See Also Properties Methods Events [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic14659.md)  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks.Components Namespace](topic13925.md) : ProjectPart Class  
---  
  
Include Inherited Members    
Include Protected Members  


Glossary Item Box

The following tables list the members exposed by [ProjectPart](topic14659.md).

# ![](dotnetimages/collapse.gif)Public Properties

| Name| Description  
---|---|---  
![Public Property](dotnetimages/publicProperty.gif)| [CapturedComponentId](topic14698.md)| Gets the unique identifier of the captured component to which the project component refers. (Inherited from [DriveWorks.SolidWorks.Components.ProjectSolidWorksComponent](topic14692.md))  
![Public Property](dotnetimages/publicProperty.gif)| [Children](topic14666.md)| Gets a collection of drawings which are children of the part.   
![Public Property](dotnetimages/publicProperty.gif)| [Configuration](topic14667.md)| Provides access to the rule and comment for the configuration.   
![Public Property](dotnetimages/publicProperty.gif)| [CustomProperties](topic14668.md)| Gets a collection of custom properties which are associated with the component.   
![Public Property](dotnetimages/publicProperty.gif)| [Dimensions](topic14669.md)| Gets a collection of dimensions which are associated with the component.   
![Public Property](dotnetimages/publicProperty.gif)| [Features](topic14670.md)| Gets a collection of features which are associated with the component.   
![Public Property](dotnetimages/publicProperty.gif)| [FileFormats](topic14671.md)| Gets a collection of file formats which are associated with the component.   
![Public Property](dotnetimages/publicProperty.gif)| [FileName](topic14699.md)| Provides access to the file name rule and comment. (Inherited from [DriveWorks.SolidWorks.Components.ProjectSolidWorksComponent](topic14692.md))  
![Public Property](dotnetimages/publicProperty.gif)| [IncludeFileFormatsInLoop](topic6192.md)| Gets/sets whether file formats should be generated in the loop. (Inherited from [DriveWorks.Components.ProjectComponent](topic6183.md))  
![Public Property](dotnetimages/publicProperty.gif)| [IsLoopEnabled](topic6193.md)| Gets/sets whether looping is enabled for this component. (Inherited from [DriveWorks.Components.ProjectComponent](topic6183.md))  
![Public Property](dotnetimages/publicProperty.gif)| [LoopCount](topic6194.md)| Gets the rule that controls how many times this component should be looped during release. (Inherited from [DriveWorks.Components.ProjectComponent](topic6183.md))  
![Public Property](dotnetimages/publicProperty.gif)| [MasterPath](topic14700.md)| Gets the master path for the component if the capture data is resolved, otherwise throws an exception. (Inherited from [DriveWorks.SolidWorks.Components.ProjectSolidWorksComponent](topic14692.md))  
![Public Property](dotnetimages/publicProperty.gif)| [RelativePath](topic14701.md)| Provides access to the relative path rule and comment. (Inherited from [DriveWorks.SolidWorks.Components.ProjectSolidWorksComponent](topic14692.md))  
![Public Property](dotnetimages/publicProperty.gif)| [Tasks](topic6195.md)| Gets the tasks associated with this component. (Inherited from [DriveWorks.Components.ProjectComponent](topic6183.md))  
Top

# ![](dotnetimages/collapse.gif)Protected Properties

| Name| Description  
---|---|---  
![Protected Property](dotnetimages/protectedProperty.gif)| [Scopes](topic14672.md)| Overridden.   
Top

# ![](dotnetimages/collapse.gif)Public Methods

| Name| Description  
---|---|---  
![Public Method](dotnetimages/publicMethod.gif)| CreateObjRef|  (Inherited from System.MarshalByRefObject)  
![Public Method](dotnetimages/publicMethod.gif)| GetLifetimeService|  (Inherited from System.MarshalByRefObject)  
Top

# ![](dotnetimages/collapse.gif)Protected Methods

| Name| Description  
---|---|---  
![Protected Method](dotnetimages/protectedMethod.gif)| [Initialize](topic14665.md)| Overridden.   
![Protected Method](dotnetimages/protectedMethod.gif)| MemberwiseClone| Overloaded. (Inherited from System.MarshalByRefObject)  
![Protected Method](dotnetimages/protectedMethod.gif)| [RaiseIsLoopChanged](topic6190.md)|  (Inherited from [DriveWorks.Components.ProjectComponent](topic6183.md))  
![Protected Method](dotnetimages/protectedMethod.gif)| [RaiseLoopFileFormatsChanged](topic6191.md)|  (Inherited from [DriveWorks.Components.ProjectComponent](topic6183.md))  
Top

# ![](dotnetimages/collapse.gif)Public Events

| Name| Description  
---|---|---  
![Public Event](dotnetimages/publicEvent.gif)| [IncludeFileFormatsInLoopChanged](topic6196.md)| Raised whenever the [DriveWorks.Components.ProjectComponent.IncludeFileFormatsInLoop](topic6192.md) property changes. (Inherited from [DriveWorks.Components.ProjectComponent](topic6183.md))  
![Public Event](dotnetimages/publicEvent.gif)| [IsLoopEnabledChanged](topic6197.md)| Raised whenever the [DriveWorks.Components.ProjectComponent.IsLoopEnabled](topic6193.md) property changes. (Inherited from [DriveWorks.Components.ProjectComponent](topic6183.md))  
Top

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ProjectPart Class](topic14659.md)   
[DriveWorks.SolidWorks.Components Namespace](topic13925.md)


