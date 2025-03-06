![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Members Options: Show All  Members Options: Filtered   
---  
DriveWorks SDK Documentation  |   
---|---  
DynamicProperty Class Members   
See Also Properties Methods [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic9398.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Forms.DataModel Namespace](topic9371.md) : DynamicProperty Class  
---  
  
Include Inherited Members    
Include Protected Members  


Glossary Item Box

The following tables list the members exposed by [DynamicProperty](topic9398.md).

# ![](dotnetimages/collapse.gif)Public Properties

| Name| Description  
---|---|---  
![Public Property](dotnetimages/publicProperty.gif)| [Behavior](topic9444.md)| Controls the dynamic behavior of the property.   
![Public Property](dotnetimages/publicProperty.gif)| [Category](topic9445.md)| Gets the category associated with the property.   
![Public Property](dotnetimages/publicProperty.gif)| [Converter](topic9446.md)| Gets the converter which handles moving the property value between the store and the control.   
![Public Property](dotnetimages/publicProperty.gif)| [CustomStoreName](topic9447.md)| Gets the name of the property in a custom store if the property isn't mapped on to a standard store.   
![Public Property](dotnetimages/publicProperty.gif)| [DefaultValue](topic9448.md)| Gets the default value of the property.   
![Public Property](dotnetimages/publicProperty.gif)| [Description](topic9449.md)| Gets a localized description of the property.   
![Public Property](dotnetimages/publicProperty.gif)| [DisplayName](topic9450.md)| Gets a localized display name for the property.   
![Public Property](dotnetimages/publicProperty.gif)| [InvalidNumberHandling](topic9451.md)| Gets how invalid values (such as System.Double) are treated in this property.   
![Public Property](dotnetimages/publicProperty.gif)| [LegacyBehaviorDefault](topic9452.md)| Gets the default value to use if this is a legacy behaviour that is now being exposed in a property.   
![Public Property](dotnetimages/publicProperty.gif)| [PropertyTypes](topic9453.md)| The semantic types of this property.   
![Public Property](dotnetimages/publicProperty.gif)| [SerializeAs](topic9454.md)| Gets the name of the property used for XML serialization/deserialization.   
![Public Property](dotnetimages/publicProperty.gif)| [StandardStoreOption](topic9455.md)| Gets the standard store to which the property is mapped if it is mapped to a standard store.   
Top

# ![](dotnetimages/collapse.gif)Public Methods

| Name| Description  
---|---|---  
![Public Method](dotnetimages/publicMethod.gif)| [CanSetIsExtended](topic9404.md)| Determines whether the property can be extended.   
![Public Method](dotnetimages/publicMethod.gif)| CreateObjRef|  (Inherited from System.MarshalByRefObject)  
![Public Method](dotnetimages/publicMethod.gif)| [GetComment](topic9405.md)|   
![Public Method](dotnetimages/publicMethod.gif)![static \(Shared in Visual Basic\)](dotnetimages/static.gif)| [GetConverter](topic9406.md)| Gets the property value converter for the given CLR type.   
![Public Method](dotnetimages/publicMethod.gif)| [GetFormula](topic9407.md)|   
![Public Method](dotnetimages/publicMethod.gif)| [GetIsExtended](topic9408.md)| Gets whether the property is extended on the given control.   
![Public Method](dotnetimages/publicMethod.gif)| GetLifetimeService|  (Inherited from System.MarshalByRefObject)  
![Public Method](dotnetimages/publicMethod.gif)![static \(Shared in Visual Basic\)](dotnetimages/static.gif)| [GetProperties](topic9409.md)| Overloaded.   
![Public Method](dotnetimages/publicMethod.gif)![static \(Shared in Visual Basic\)](dotnetimages/static.gif)| [GetStandardStoreName](topic9412.md)| Overloaded. Gets the reference name that will be used for the specified control name and store option combination.   
![Public Method](dotnetimages/publicMethod.gif)| [GetStoreName](topic9415.md)| Overloaded. Gets the store name for a dynamic extended property.   
![Public Method](dotnetimages/publicMethod.gif)| [GetStoreValue](topic9418.md)| Gets the current unconverted value of the property from the specified control.   
![Public Method](dotnetimages/publicMethod.gif)| [GetValue](topic9419.md)| Overloaded. Gets the current value of the property from the specified control, and converts it to the proper type.   
![Public Method](dotnetimages/publicMethod.gif)| [GetVersionHistory](topic9422.md)| Returns the rule and comment history for given control.   
![Public Method](dotnetimages/publicMethod.gif)| [HasFormula](topic9423.md)|   
![Public Method](dotnetimages/publicMethod.gif)| [IsDynamic](topic9424.md)| Determines whether the property is dynamic.   
![Public Method](dotnetimages/publicMethod.gif)| [IsDynamicNotNoRule](topic9425.md)| Determines whether the property is dynamic, and doesn't have the [PropertyBehavior.FlagNoRuleAllowed](topic9383.md) flag set.   
![Public Method](dotnetimages/publicMethod.gif)| [IsRegisteredToControl](topic9426.md)| Determines whether the given control has this [DynamicProperty](topic9398.md) registered to it.   
![Public Method](dotnetimages/publicMethod.gif)![static \(Shared in Visual Basic\)](dotnetimages/static.gif)| [OverrideDefaultValue](topic9427.md)| Overrides the default value of the property for the given type, which derives from the type which defines the property.   
![Public Method](dotnetimages/publicMethod.gif)![static \(Shared in Visual Basic\)](dotnetimages/static.gif)| [Register](topic9428.md)| Overloaded. Registers a dynamic property for the given type of control.   
![Public Method](dotnetimages/publicMethod.gif)![static \(Shared in Visual Basic\)](dotnetimages/static.gif)| [RegisterStatic](topic9435.md)| Overloaded. Registers a static property, which has the same backing store name as serialization name, for the given type of control.   
![Public Method](dotnetimages/publicMethod.gif)![static \(Shared in Visual Basic\)](dotnetimages/static.gif)| [RemoveProperty](topic9438.md)| Removes a dynamic property from the list of properties for the given control.   
![Public Method](dotnetimages/publicMethod.gif)| [SetComment](topic9439.md)|   
![Public Method](dotnetimages/publicMethod.gif)| [SetFormula](topic9440.md)|   
![Public Method](dotnetimages/publicMethod.gif)| [SetIsExtended](topic9441.md)| Sets whether the property is extended on the given control.   
![Public Method](dotnetimages/publicMethod.gif)| [SetRuleAndComment](topic9442.md)|   
![Public Method](dotnetimages/publicMethod.gif)| [SetValue](topic9443.md)| Sets the value of the property on the specified control.   
Top

# ![](dotnetimages/collapse.gif)Protected Methods

| Name| Description  
---|---|---  
![Protected Method](dotnetimages/protectedMethod.gif)| MemberwiseClone| Overloaded. (Inherited from System.MarshalByRefObject)  
Top

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[DynamicProperty Class](topic9398.md)   
[DriveWorks.Forms.DataModel Namespace](topic9371.md)


