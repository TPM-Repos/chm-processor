![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Members Options: Show All  Members Options: Filtered   
---  
DriveWorks SDK Documentation  |   
---|---  
ProjectVariable Class Members   
See Also Properties Methods Events [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic4927.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) : ProjectVariable Class  
---  
  
Include Inherited Members    
Include Protected Members  


Glossary Item Box

The following tables list the members exposed by [ProjectVariable](topic4927.md).

# ![](dotnetimages/collapse.gif)Public Properties

| Name| Description  
---|---|---  
![Public Property](dotnetimages/publicProperty.gif)| [Comment](topic4950.md)| Gets/sets the comment for the variable.   
![Public Property](dotnetimages/publicProperty.gif)| [DisplayName](topic4951.md)| Gets/sets the display name of the variable.   
![Public Property](dotnetimages/publicProperty.gif)| [Id](topic4952.md)| Gets the invariant identifier of the rule.   
![Public Property](dotnetimages/publicProperty.gif)| [IsDeleted](topic4953.md)| Gets whether the variable has been deleted.   
![Public Property](dotnetimages/publicProperty.gif)| [Name](topic4954.md)| Gets the name of the variable in a form which can be used in rules.   
![Public Property](dotnetimages/publicProperty.gif)| [Parent](topic4955.md)| Gets/sets the category to which the variable belongs.   
![Public Property](dotnetimages/publicProperty.gif)| [Project](topic4956.md)| Gets the project.   
![Public Property](dotnetimages/publicProperty.gif)| [Rule](topic4957.md)| Gets/sets the rule which governs the variable's value.   
![Public Property](dotnetimages/publicProperty.gif)| [Text](topic4958.md)| Gets a textual representation of the variable's current value.   
![Public Property](dotnetimages/publicProperty.gif)| [Value](topic4959.md)| Gets the current value of the variable.   
Top

# ![](dotnetimages/collapse.gif)Public Methods

| Name| Description  
---|---|---  
![Public Method](dotnetimages/publicMethod.gif)| CreateObjRef|  (Inherited from System.MarshalByRefObject)  
![Public Method](dotnetimages/publicMethod.gif)| [Delete](topic4934.md)| Deletes the variable   
![Public Method](dotnetimages/publicMethod.gif)| [EnumerateVersionHistory](topic4937.md)| Gets the version history for the variable.   
![Public Method](dotnetimages/publicMethod.gif)| GetLifetimeService|  (Inherited from System.MarshalByRefObject)  
![Public Method](dotnetimages/publicMethod.gif)| [GetVersionHistory](topic4938.md)| Gets the version history for the variable.   
![Public Method](dotnetimages/publicMethod.gif)| [Serialize](topic4946.md)| Serializes this [ProjectVariable](topic4927.md) to the provided System.Xml.XmlWriter.   
![Public Method](dotnetimages/publicMethod.gif)| [SetRuleAndComment](topic4949.md)| Sets the rule and comment in a single operation.   
Top

# ![](dotnetimages/collapse.gif)Protected Methods

| Name| Description  
---|---|---  
![Protected Method](dotnetimages/protectedMethod.gif)| [ConnectValueChangedEvent](topic4933.md)|   
![Protected Method](dotnetimages/protectedMethod.gif)| [DeleteCore](topic4935.md)| Performs the work of deleting the variable from the backing store.   
![Protected Method](dotnetimages/protectedMethod.gif)| [DisconnectValueChangedEvent](topic4936.md)|   
![Protected Method](dotnetimages/protectedMethod.gif)| MemberwiseClone| Overloaded. (Inherited from System.MarshalByRefObject)  
![Protected Method](dotnetimages/protectedMethod.gif)| [RaiseCategoryChanged](topic4939.md)|   
![Protected Method](dotnetimages/protectedMethod.gif)| [RaiseCommentChanged](topic4940.md)|   
![Protected Method](dotnetimages/protectedMethod.gif)| [RaiseDeleted](topic4941.md)|   
![Protected Method](dotnetimages/protectedMethod.gif)| [RaiseNameChanged](topic4942.md)|   
![Protected Method](dotnetimages/protectedMethod.gif)| [RaiseRuleChanged](topic4943.md)|   
![Protected Method](dotnetimages/protectedMethod.gif)| [RaiseValueChanged](topic4944.md)|   
![Protected Method](dotnetimages/protectedMethod.gif)| [SaveVersion](topic4945.md)| Adds an entry to the variable's history.   
![Protected Method](dotnetimages/protectedMethod.gif)| [SetCategoryCore](topic4947.md)|   
![Protected Method](dotnetimages/protectedMethod.gif)| [SetDisplayNameCore](topic4948.md)|   
Top

# ![](dotnetimages/collapse.gif)Public Events

| Name| Description  
---|---|---  
![Public Event](dotnetimages/publicEvent.gif)| [CommentChanged](topic4960.md)| Raised when the variable's comment is changed.   
![Public Event](dotnetimages/publicEvent.gif)| [Deleted](topic4961.md)| Raised when the variable is deleted.   
![Public Event](dotnetimages/publicEvent.gif)| [NameChanged](topic4962.md)| Raised when the name of the variable is changed.   
![Public Event](dotnetimages/publicEvent.gif)| [ParentChanged](topic4963.md)| Raised when the variable's category is changed.   
![Public Event](dotnetimages/publicEvent.gif)| [RuleChanged](topic4964.md)| Raised when the rule which defines the variable value changes.   
![Public Event](dotnetimages/publicEvent.gif)| [ValueChanged](topic4965.md)| Raised when the value of the variable changes.   
Top

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ProjectVariable Class](topic4927.md)   
[DriveWorks Namespace](topic2159.md)


