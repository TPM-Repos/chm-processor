![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Members Options: Show All  Members Options: Filtered   
---  
DriveWorks SDK Documentation  |   
---|---  
ProjectCalculationTableColumn Class Members   
See Also Properties Methods Events [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic3946.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) : ProjectCalculationTableColumn Class  
---  
  
Include Inherited Members    
Include Protected Members  


Glossary Item Box

The following tables list the members exposed by [ProjectCalculationTableColumn](topic3946.md).

# ![](dotnetimages/collapse.gif)Public Properties

| Name| Description  
---|---|---  
![Public Property](dotnetimages/publicProperty.gif)| [CommonRule](topic3961.md)| The common rule that will be used for all cells that don't have an explicit rule set on them.   
![Public Property](dotnetimages/publicProperty.gif)| [DisplayName](topic3962.md)| The display name of the column.   
![Public Property](dotnetimages/publicProperty.gif)| [Index](topic3963.md)| The zero based index of the this column.   
![Public Property](dotnetimages/publicProperty.gif)| [Name](topic3964.md)| The name of the column.   
![Public Property](dotnetimages/publicProperty.gif)| [Type](topic3965.md)| The type of the column.   
Top

# ![](dotnetimages/collapse.gif)Public Methods

| Name| Description  
---|---|---  
Public Method| CreateObjRef|  (Inherited from System.MarshalByRefObject)  
Public Method![static \(Shared in Visual Basic\)](dotnetimages/static.gif)| [GetCellReferenceName](topic3952.md)| Converts a column display name to a rule reference name that can be used within a table only.   
Public Method| [GetContext](topic3953.md)| Gets a rule context for a particular cell. This is useful when evaluating common with the context of a specific cell.   
Public Method| [GetEnumerator](topic3954.md)| Gets an IEnumerator that will yield all explicitly set cell rules.   
Public Method![static \(Shared in Visual Basic\)](dotnetimages/static.gif)| [GetFullCellReferenceName](topic3955.md)| Gets a full rule reference name (including the table name) to the specified cell.   
Public Method| [GetFullRuleId](topic3956.md)| Gets a rule reference for the specified cell.   
Public Method| GetLifetimeService|  (Inherited from System.MarshalByRefObject)  
Public Method![static \(Shared in Visual Basic\)](dotnetimages/static.gif)| [GetName](topic3957.md)| Converts a column display name to a column name.   
Public Method| [GetRule](topic3958.md)| Gets an explicit rule from this column for the specified row.   
Public Method| [GetRules](topic3959.md)| Get's all cell rules that re explicitly set in the column.   
Public Method| [RemoveRule](topic3960.md)| Clears a cell rule at the specified index, causing it to use the column's common rule.   
Top

# ![](dotnetimages/collapse.gif)Protected Methods

| Name| Description  
---|---|---  
Protected Method| MemberwiseClone| Overloaded. (Inherited from System.MarshalByRefObject)  
Top

# ![](dotnetimages/collapse.gif)Public Events

| Name| Description  
---|---|---  
![Public Event](dotnetimages/publicEvent.gif)| [CollectionChanged](topic3966.md)| Raised when the collection of explicit cell rules in this column changes.   
![Public Event](dotnetimages/publicEvent.gif)| [PropertyChanged](topic3967.md)| Raised when a property is changed, such as name or type.   
Top

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ProjectCalculationTableColumn Class](topic3946.md)   
[DriveWorks Namespace](topic2159.md)


