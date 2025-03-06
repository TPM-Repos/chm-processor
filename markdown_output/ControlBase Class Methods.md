![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Members Options: Show All  Members Options: Filtered   
---  
DriveWorks SDK Documentation  |   
---|---  
ControlBase Class Methods   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic7698.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Forms Namespace](topic7266.md) : ControlBase Class  
---  
  
Include Inherited Members    
Include Protected Members    


Glossary Item Box

For a list of all members of this type, see [ControlBase members](topic7699.md).

# ![](dotnetimages/collapse.gif)Public Methods

| Name| Description  
---|---|---  
![Public Method](dotnetimages/publicMethod.gif)| [ClearInputValue](topic7705.md)| Clears the input value of the control, if it has one.   
![Public Method](dotnetimages/publicMethod.gif)| CreateObjRef|  (Inherited from System.MarshalByRefObject)  
![Public Method](dotnetimages/publicMethod.gif)| [CreateRefactorProcess](topic7706.md)| Creates an object capable of refactoring all references to the control from its current name, to the given new name.   
![Public Method](dotnetimages/publicMethod.gif)| [GetDefaultRule](topic7707.md)| Gets the default rule for the control's input property.   
![Public Method](dotnetimages/publicMethod.gif)| [GetInputValue](topic7708.md)| Returns the current input value of the control, if has one.   
![Public Method](dotnetimages/publicMethod.gif)| GetLifetimeService|  (Inherited from System.MarshalByRefObject)  
![Public Method](dotnetimages/publicMethod.gif)| [IsValidParent](topic7709.md)| Validates whether the control can be added to the specified parent.   
![Public Method](dotnetimages/publicMethod.gif)| [Rename](topic7717.md)| Renames the control.   
![Public Method](dotnetimages/publicMethod.gif)| [Serialize](topic7718.md)| Serializes the control and any contents to the given XML writer.   
![Public Method](dotnetimages/publicMethod.gif)| [SetInputValue](topic7720.md)| Overloaded. Sets the current input value of the control, if it has one.   
![Public Method](dotnetimages/publicMethod.gif)| [WithTransientEvent](topic7725.md)| Attaches the given event to the given property of the control so that changes to the property will include the event details, and returns an implementation of System.IDisposable that will detach when it is disposed.   
Top

# ![](dotnetimages/collapse.gif)Protected Methods

| Name| Description  
---|---|---  
![Protected Method](dotnetimages/protectedMethod.gif)| [AssertInSpecification](topic7704.md)| Throws an invalid operation exception if there is no active specification.   
![Protected Method](dotnetimages/protectedMethod.gif)| MemberwiseClone| Overloaded. (Inherited from System.MarshalByRefObject)  
![Protected Method](dotnetimages/protectedMethod.gif)| [OnDataProviderInitialized](topic7710.md)| Called when the DataProvider for this control has been initialized.   
![Protected Method](dotnetimages/protectedMethod.gif)| [OnDeleted](topic7711.md)| Raises the [Deleted](topic7759.md) event.   
![Protected Method](dotnetimages/protectedMethod.gif)| [OnInitialized](topic7712.md)| Raises the [Initialized](topic7760.md) event.   
![Protected Method](dotnetimages/protectedMethod.gif)| [OnParentDefaultFontChanged](topic7713.md)| Gives child controls a chance to update the font properties when the default font changed.   
![Protected Method](dotnetimages/protectedMethod.gif)| [OnValidated](topic7714.md)| Raises the [Validated](topic7764.md) event.   
![Protected Method](dotnetimages/protectedMethod.gif)| [OnValueChanged](topic7715.md)| Raises the [OnValueChanged](topic7715.md) event.   
![Protected Method](dotnetimages/protectedMethod.gif)| [RaiseLayoutChanged](topic7716.md)| Raises the [LayoutChanged](topic7761.md) event.   
![Protected Method](dotnetimages/protectedMethod.gif)| [SerializeCore](topic7719.md)| Serializes the contents of the control.   
![Protected Method](dotnetimages/protectedMethod.gif)| [TryExecuteOnChangeMacro](topic7723.md)|   
![Protected Method](dotnetimages/protectedMethod.gif)| [Validate](topic7724.md)| When overridden by a derived control, validates the control's properties after a change.   
Top

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ControlBase Class](topic7698.md)   
[DriveWorks.Forms Namespace](topic7266.md)

©2024 DriveWorks Ltd. All Rights Reserved.
