Collapse All Expand All Members Options: Show All  Members Options: Filtered   
---  
DriveWorks SDK Documentation  |   
---|---  
OptionGroup Class Methods   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Forms Namespace](topic7266.md) : OptionGroup Class  
---  
  
Include Inherited Members    
Include Protected Members    


Glossary Item Box

For a list of all members of this type, see [OptionGroup members](topic8609.md).

# Public Methods

| Name| Description  
---|---|---  
Public Method| [ClearInputValue](topic8615.md)| Overridden. Sets the selected item to null.   
Public Method| CreateObjRef|  (Inherited from System.MarshalByRefObject)  
Public Method| [CreateRefactorProcess](topic7706.md)| Creates an object capable of refactoring all references to the control from its current name, to the given new name. (Inherited from [DriveWorks.Forms.ControlBase](topic7698.md))  
Public Method| [GetDefaultRule](topic7707.md)| Gets the default rule for the control's input property. (Inherited from [DriveWorks.Forms.ControlBase](topic7698.md))  
Public Method| [GetInputValue](topic8616.md)| Overridden. Returns the current selected item of the control.   
Public Method| GetLifetimeService|  (Inherited from System.MarshalByRefObject)  
Public Method| [IsValidParent](topic7709.md)| Validates whether the control can be added to the specified parent. (Inherited from [DriveWorks.Forms.ControlBase](topic7698.md))  
Public Method| [Rename](topic7717.md)| Renames the control. (Inherited from [DriveWorks.Forms.ControlBase](topic7698.md))  
Public Method| [Serialize](topic7718.md)| Serializes the control and any contents to the given XML writer. (Inherited from [DriveWorks.Forms.ControlBase](topic7698.md))  
Public Method| [SetInputValue](topic8620.md)| Overloaded. Overridden. Sets the selected item of the control.   
Public Method| [SetSelectedItem](topic8322.md)| Sets the [ListControlBase](topic8315.md)'s [SelectedItemSourceProperty](topic8339.md) and temporarily registers the source of this change. (Inherited from [DriveWorks.Forms.ListControlBase](topic8315.md))  
Public Method| [WithTransientEvent](topic7725.md)| Attaches the given event to the given property of the control so that changes to the property will include the event details, and returns an implementation of System.IDisposable that will detach when it is disposed. (Inherited from [DriveWorks.Forms.ControlBase](topic7698.md))  
Top

# Protected Methods

| Name| Description  
---|---|---  
Protected Method| [AssertInSpecification](topic7704.md)| Throws an invalid operation exception if there is no active specification. (Inherited from [DriveWorks.Forms.ControlBase](topic7698.md))  
Protected Method| MemberwiseClone| Overloaded. (Inherited from System.MarshalByRefObject)  
Protected Method| [OnDataProviderInitialized](topic8617.md)| Overridden.   
Protected Method| [OnDeleted](topic7711.md)| Raises the [Deleted](topic7759.md) event. (Inherited from [DriveWorks.Forms.ControlBase](topic7698.md))  
Protected Method| [OnInitialized](topic7712.md)| Raises the [Initialized](topic7760.md) event. (Inherited from [DriveWorks.Forms.ControlBase](topic7698.md))  
Protected Method| [OnParentDefaultFontChanged](topic8618.md)| Overridden.   
Protected Method| [OnValidated](topic7714.md)| Raises the [Validated](topic7764.md) event. (Inherited from [DriveWorks.Forms.ControlBase](topic7698.md))  
Protected Method| [OnValueChanged](topic8619.md)| Overridden.   
Protected Method| [RaiseLayoutChanged](topic7716.md)| Raises the [LayoutChanged](topic7761.md) event. (Inherited from [DriveWorks.Forms.ControlBase](topic7698.md))  
Protected Method| [SerializeCore](topic7719.md)| Serializes the contents of the control. (Inherited from [DriveWorks.Forms.ControlBase](topic7698.md))  
Protected Method| [TryExecuteOnChangeMacro](topic7723.md)|  (Inherited from [DriveWorks.Forms.ControlBase](topic7698.md))  
Protected Method| [Validate](topic8323.md)| Overridden to validate the selected item. (Inherited from [DriveWorks.Forms.ListControlBase](topic8315.md))  
Top

# See Also

#### Reference

[OptionGroup Class](topic8608.md)   
[DriveWorks.Forms Namespace](topic7266.md)


