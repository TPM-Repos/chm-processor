Collapse All Expand All Members Options: Show All  Members Options: Filtered   
---  
DriveWorks SDK Documentation  |   
---|---  
ISolidWorksState Interface Members   
See Also Properties Methods Events [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic13419.md)  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks Namespace](topic13345.md) : ISolidWorksState Interface  
---  
  
Include Inherited Members    


Glossary Item Box

The following tables list the members exposed by [ISolidWorksState](topic13419.md).

# Public Properties

| Name| Description  
---|---|---  
![ Property](dotnetimages/Property.gif)| [CapturedComponent](topic13430.md)| Gets/sets the capture information for the current model.   
![ Property](dotnetimages/Property.gif)| [CapturedComponentHandle](topic13431.md)| Gets/sets the handle to the capture information for the current model.   
Top

# Public Methods

| Name| Description  
---|---|---  
![ Method](dotnetimages/Method.gif)| [GetModel<T>](topic13424.md)| Gets the model currently open in SolidWorks. The type of it is one of the derivatives of ModelDoc2, AssemblyDoc/PartDoc/DrawingDoc.   
![ Method](dotnetimages/Method.gif)| [GetModelChildComponents<T>](topic13425.md)| Gets all the features and referenced components in the current model.   
![ Method](dotnetimages/Method.gif)| [GetModelComponent<T>](topic13426.md)| Gets the root component for the current model.   
![ Method](dotnetimages/Method.gif)| [GetModelExtension<T>](topic13427.md)| Gets the extension of the model currently loaded in SolidWorks.   
![ Method](dotnetimages/Method.gif)| [GetModelType<T>](topic13428.md)| The type of the Model currently loaded in SolidWorks.   
![ Method](dotnetimages/Method.gif)| [GetSelectionManager<T>](topic13429.md)| The selection manager used to track the current selection in SolidWorks.   
Top

# Public Events

| Name| Description  
---|---|---  
![ Event](dotnetimages/Event.gif)| [ActiveConfigChangePostNotify](topic13432.md)| Raised when the configuration of the current Assembly changed.   
![ Event](dotnetimages/Event.gif)| [ActiveModelDocChangeNotify](topic13433.md)| Raised by SolidWorks when the active model document has changed.   
![ Event](dotnetimages/Event.gif)| [CapturedComponentChanged](topic13434.md)| Raised whenever the [CapturedComponent](topic13430.md) property changes.   
![ Event](dotnetimages/Event.gif)| [DestroyNotify](topic13435.md)| Provides pre-notification that a document is closing.   
![ Event](dotnetimages/Event.gif)| [FileOpenPostNotify](topic13436.md)| Raised by SolidWorks after a file has been opened.   
![ Event](dotnetimages/Event.gif)| [FileOpenPreNotify](topic13437.md)| Raised by SolidWorks before a file has been opened.   
![ Event](dotnetimages/Event.gif)| [FileSavePostNotify](topic13438.md)| Post-notifies the user program when a file is saved in SolidWorks.   
![ Event](dotnetimages/Event.gif)| [NewSelectionNotify](topic13439.md)| Post-notifies the user program when the selection list has changed.   
Top

# See Also

#### Reference

[ISolidWorksState Interface](topic13419.md)   
[DriveWorks.SolidWorks Namespace](topic13345.md)


