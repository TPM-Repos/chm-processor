![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Members Options: Show All  Members Options: Filtered   
---  
DriveWorks SDK Documentation  |   
---|---  
Form Class Methods   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Forms Namespace](topic7266.md) : Form Class  
---  
  
Include Inherited Members    
Include Protected Members    


Glossary Item Box

For a list of all members of this type, see [Form members](topic8087.md).

# ![](dotnetimages/collapse.gif)Public Methods

| Name| Description  
---|---|---  
Public Method| [ClearInputValue](topic7705.md)| Clears the input value of the control, if it has one. (Inherited from [DriveWorks.Forms.ControlBase](topic7698.md))  
Public Method| CreateObjRef|  (Inherited from System.MarshalByRefObject)  
Public Method| [CreateRefactorProcess](topic7706.md)| Creates an object capable of refactoring all references to the control from its current name, to the given new name. (Inherited from [DriveWorks.Forms.ControlBase](topic7698.md))  
Public Method| [DeleteControls](topic8092.md)| Overloaded. Deletes the specified control from the form.   
Public Method| [GetAllControls](topic7691.md)| Gets collection of all child controls contained by the control. Including the control children's children. (Inherited from [DriveWorks.Forms.ContainerControlBase](topic7684.md))  
Public Method| [GetDefaultRule](topic7707.md)| Gets the default rule for the control's input property. (Inherited from [DriveWorks.Forms.ControlBase](topic7698.md))  
Public Method| [GetInputValue](topic7708.md)| Returns the current input value of the control, if has one. (Inherited from [DriveWorks.Forms.ControlBase](topic7698.md))  
Public Method| GetLifetimeService|  (Inherited from System.MarshalByRefObject)  
Public Method| [IsValidChild](topic7692.md)| Validates whether the specified control can be added as a child. (Inherited from [DriveWorks.Forms.ContainerControlBase](topic7684.md))  
Public Method| [IsValidParent](topic8095.md)| Overridden. Overridden to prevent parenting the form to any other control.   
Public Method| [Serialize](topic7718.md)| Serializes the control and any contents to the given XML writer. (Inherited from [DriveWorks.Forms.ControlBase](topic7698.md))  
Public Method| [SetInputValue](topic7720.md)| Overloaded. Sets the current input value of the control, if it has one. (Inherited from [DriveWorks.Forms.ControlBase](topic7698.md))  
Public Method| [WithTransientEvent](topic7725.md)| Attaches the given event to the given property of the control so that changes to the property will include the event details, and returns an implementation of System.IDisposable that will detach when it is disposed. (Inherited from [DriveWorks.Forms.ControlBase](topic7698.md))  
Top

# ![](dotnetimages/collapse.gif)Protected Methods

| Name| Description  
---|---|---  
Protected Method| [AssertInSpecification](topic7704.md)| Throws an invalid operation exception if there is no active specification. (Inherited from [DriveWorks.Forms.ControlBase](topic7698.md))  
Protected Method| MemberwiseClone| Overloaded. (Inherited from System.MarshalByRefObject)  
Protected Method| [OnDataProviderInitialized](topic7710.md)| Called when the DataProvider for this control has been initialized. (Inherited from [DriveWorks.Forms.ControlBase](topic7698.md))  
Protected Method| [OnDeleted](topic7693.md)| Raises the [Deleted](topic7759.md) event. (Inherited from [DriveWorks.Forms.ContainerControlBase](topic7684.md))  
Protected Method| [OnInitialized](topic7712.md)| Raises the [Initialized](topic7760.md) event. (Inherited from [DriveWorks.Forms.ControlBase](topic7698.md))  
Protected Method| [OnParentDefaultFontChanged](topic7713.md)| Gives child controls a chance to update the font properties when the default font changed. (Inherited from [DriveWorks.Forms.ControlBase](topic7698.md))  
Protected Method| [OnValidated](topic7714.md)| Raises the [Validated](topic7764.md) event. (Inherited from [DriveWorks.Forms.ControlBase](topic7698.md))  
Protected Method| [OnValueChanged](topic7715.md)| Raises the [OnValueChanged](topic7715.md) event. (Inherited from [DriveWorks.Forms.ControlBase](topic7698.md))  
Protected Method| [RaiseLayoutChanged](topic7716.md)| Raises the [LayoutChanged](topic7761.md) event. (Inherited from [DriveWorks.Forms.ControlBase](topic7698.md))  
Protected Method| [SerializeCore](topic7694.md)| Overridden to serialize child controls. (Inherited from [DriveWorks.Forms.ContainerControlBase](topic7684.md))  
Protected Method| [TryExecuteOnChangeMacro](topic7723.md)|  (Inherited from [DriveWorks.Forms.ControlBase](topic7698.md))  
Protected Method| [Validate](topic7724.md)| When overridden by a derived control, validates the control's properties after a change. (Inherited from [DriveWorks.Forms.ControlBase](topic7698.md))  
Top

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[Form Class](topic8086.md)   
[DriveWorks.Forms Namespace](topic7266.md)


