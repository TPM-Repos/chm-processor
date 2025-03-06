TinyMCEControl Class Methods   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Forms Namespace](topic7266.md) : TinyMCEControl Class  
---  
  
Include Inherited Members    
Include Protected Members    


Glossary Item Box

For a list of all members of this type, see [TinyMCEControl members](topic9205.md).

# Public Methods

| Name| Description  
---|---|---  
![Public Method](dotnetimages/publicMethod.gif)| [ClearInputValue](topic9210.md)| Overridden. Sets the control's HTML to an empty string.   
![Public Method](dotnetimages/publicMethod.gif)| CreateObjRef|  (Inherited from System.MarshalByRefObject)  
![Public Method](dotnetimages/publicMethod.gif)| [CreateRefactorProcess](topic7706.md)| Creates an object capable of refactoring all references to the control from its current name, to the given new name. (Inherited from [DriveWorks.Forms.ControlBase](topic7698.md))  
![Public Method](dotnetimages/publicMethod.gif)| [GetAllowedFileExtensions](topic9211.md)| Gets a list of extensions for the files that are allowed to be uploaded with this control.   
![Public Method](dotnetimages/publicMethod.gif)| [GetDefaultRule](topic7707.md)| Gets the default rule for the control's input property. (Inherited from [DriveWorks.Forms.ControlBase](topic7698.md))  
![Public Method](dotnetimages/publicMethod.gif)| [GetInputValue](topic9212.md)| Overridden. Returns the HTML value of the control.   
![Public Method](dotnetimages/publicMethod.gif)| GetLifetimeService|  (Inherited from System.MarshalByRefObject)  
![Public Method](dotnetimages/publicMethod.gif)| [HandleUpload](topic9213.md)| Takes the specified inputs and completes the upload process for this control asynchronously.   
![Public Method](dotnetimages/publicMethod.gif)| [IsValidParent](topic7709.md)| Validates whether the control can be added to the specified parent. (Inherited from [DriveWorks.Forms.ControlBase](topic7698.md))  
![Public Method](dotnetimages/publicMethod.gif)| [RejectUpload](topic9216.md)| Sets the IsUploadRejectedProperty to True.   
![Public Method](dotnetimages/publicMethod.gif)| [Rename](topic7717.md)| Renames the control. (Inherited from [DriveWorks.Forms.ControlBase](topic7698.md))  
![Public Method](dotnetimages/publicMethod.gif)| [ResetFinalUploadedFilePath](topic9217.md)| Resets the FinalUploadedFilePathProperty to an empty string.   
![Public Method](dotnetimages/publicMethod.gif)| [ResetIsUploadRejected](topic9218.md)| Resets the IsUploadRejectedProperty back to False (its default state).   
![Public Method](dotnetimages/publicMethod.gif)| [Serialize](topic7718.md)| Serializes the control and any contents to the given XML writer. (Inherited from [DriveWorks.Forms.ControlBase](topic7698.md))  
![Public Method](dotnetimages/publicMethod.gif)| [SetInputValue](topic9219.md)| Overloaded. Overridden. Sets the HTML value of the control.   
![Public Method](dotnetimages/publicMethod.gif)| [TryGetUploadFileSizeLimitInBytes](topic9221.md)| Returns the value of the [UploadFileSizeLimit](topic9242.md) property converted to bytes.   
![Public Method](dotnetimages/publicMethod.gif)| [WithTransientEvent](topic7725.md)| Attaches the given event to the given property of the control so that changes to the property will include the event details, and returns an implementation of System.IDisposable that will detach when it is disposed. (Inherited from [DriveWorks.Forms.ControlBase](topic7698.md))  
Top

# Protected Methods

| Name| Description  
---|---|---  
![Protected Method](dotnetimages/protectedMethod.gif)| [AssertInSpecification](topic7704.md)| Throws an invalid operation exception if there is no active specification. (Inherited from [DriveWorks.Forms.ControlBase](topic7698.md))  
![Protected Method](dotnetimages/protectedMethod.gif)| MemberwiseClone| Overloaded. (Inherited from System.MarshalByRefObject)  
![Protected Method](dotnetimages/protectedMethod.gif)| [OnDataProviderInitialized](topic9214.md)| Overridden.   
![Protected Method](dotnetimages/protectedMethod.gif)| [OnDeleted](topic7711.md)| Raises the [Deleted](topic7759.md) event. (Inherited from [DriveWorks.Forms.ControlBase](topic7698.md))  
![Protected Method](dotnetimages/protectedMethod.gif)| [OnInitialized](topic7712.md)| Raises the [Initialized](topic7760.md) event. (Inherited from [DriveWorks.Forms.ControlBase](topic7698.md))  
![Protected Method](dotnetimages/protectedMethod.gif)| [OnParentDefaultFontChanged](topic7713.md)| Gives child controls a chance to update the font properties when the default font changed. (Inherited from [DriveWorks.Forms.ControlBase](topic7698.md))  
![Protected Method](dotnetimages/protectedMethod.gif)| [OnValidated](topic7714.md)| Raises the [Validated](topic7764.md) event. (Inherited from [DriveWorks.Forms.ControlBase](topic7698.md))  
![Protected Method](dotnetimages/protectedMethod.gif)| [OnValueChanged](topic9215.md)| Overridden.   
![Protected Method](dotnetimages/protectedMethod.gif)| [RaiseLayoutChanged](topic7716.md)| Raises the [LayoutChanged](topic7761.md) event. (Inherited from [DriveWorks.Forms.ControlBase](topic7698.md))  
![Protected Method](dotnetimages/protectedMethod.gif)| [SerializeCore](topic7719.md)| Serializes the contents of the control. (Inherited from [DriveWorks.Forms.ControlBase](topic7698.md))  
![Protected Method](dotnetimages/protectedMethod.gif)| [TryExecuteOnChangeMacro](topic7723.md)|  (Inherited from [DriveWorks.Forms.ControlBase](topic7698.md))  
![Protected Method](dotnetimages/protectedMethod.gif)| [Validate](topic9222.md)| Overridden.   
Top

# See Also

#### Reference

[TinyMCEControl Class](topic9204.md)   
[DriveWorks.Forms Namespace](topic7266.md)


