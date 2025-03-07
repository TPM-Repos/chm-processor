Collapse All Expand All Members Options: Show All  Members Options: Filtered   
---  
DriveWorks SDK Documentation  |   
---|---  
ControlBase Class Methods   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Forms Namespace](topic7266.md) : ControlBase Class  
---  
  
Include Inherited Members    
Include Protected Members    


Glossary Item Box

For a list of all members of this type, see [ControlBase members](topic7699.md).

# Public Methods

| Name| Description  
---|---|---  
Public Method| [ClearInputValue](topic7705.md)| Clears the input value of the control, if it has one.   
Public Method| CreateObjRef|  (Inherited from System.MarshalByRefObject)  
Public Method| [CreateRefactorProcess](topic7706.md)| Creates an object capable of refactoring all references to the control from its current name, to the given new name.   
Public Method| [GetDefaultRule](topic7707.md)| Gets the default rule for the control's input property.   
Public Method| [GetInputValue](topic7708.md)| Returns the current input value of the control, if has one.   
Public Method| GetLifetimeService|  (Inherited from System.MarshalByRefObject)  
Public Method| [IsValidParent](topic7709.md)| Validates whether the control can be added to the specified parent.   
Public Method| [Rename](topic7717.md)| Renames the control.   
Public Method| [Serialize](topic7718.md)| Serializes the control and any contents to the given XML writer.   
Public Method| [SetInputValue](topic7720.md)| Overloaded. Sets the current input value of the control, if it has one.   
Public Method| [WithTransientEvent](topic7725.md)| Attaches the given event to the given property of the control so that changes to the property will include the event details, and returns an implementation of System.IDisposable that will detach when it is disposed.   
Top

# Protected Methods

| Name| Description  
---|---|---  
Protected Method| [AssertInSpecification](topic7704.md)| Throws an invalid operation exception if there is no active specification.   
Protected Method| MemberwiseClone| Overloaded. (Inherited from System.MarshalByRefObject)  
Protected Method| [OnDataProviderInitialized](topic7710.md)| Called when the DataProvider for this control has been initialized.   
Protected Method| [OnDeleted](topic7711.md)| Raises the [Deleted](topic7759.md) event.   
Protected Method| [OnInitialized](topic7712.md)| Raises the [Initialized](topic7760.md) event.   
Protected Method| [OnParentDefaultFontChanged](topic7713.md)| Gives child controls a chance to update the font properties when the default font changed.   
Protected Method| [OnValidated](topic7714.md)| Raises the [Validated](topic7764.md) event.   
Protected Method| [OnValueChanged](topic7715.md)| Raises the [OnValueChanged](topic7715.md) event.   
Protected Method| [RaiseLayoutChanged](topic7716.md)| Raises the [LayoutChanged](topic7761.md) event.   
Protected Method| [SerializeCore](topic7719.md)| Serializes the contents of the control.   
Protected Method| [TryExecuteOnChangeMacro](topic7723.md)|   
Protected Method| [Validate](topic7724.md)| When overridden by a derived control, validates the control's properties after a change.   
Top

# See Also

#### Reference

[ControlBase Class](topic7698.md)   
[DriveWorks.Forms Namespace](topic7266.md)


