![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateTxSetCalculationTableColumnRowRule Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic13133.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Transactions Namespace](topic12835.md) > [ProjectTransactionFactory Class](topic12928.md) : CreateTxSetCalculationTableColumnRowRule Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_tableName_
    The name of the table to use.

_columnName_
    The name of the column to use.

_rowIndex_
    The row index of the cell to set.

_rule_
    The rule to set in the cell.

_comment_
    The comment to set on the cell.

Glossary Item Box

Creates a transaction that will set the rule of a calculation table's cell. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function CreateTxSetCalculationTableColumnRowRule( _
       ByVal _tableName_ As String, _
       ByVal _columnName_ As String, _
       ByVal _rowIndex_ As Integer, _
       ByVal _rule_ As String, _
       ByVal _comment_ As String _
    ) As [ITransaction](topic12837.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ProjectTransactionFactory](topic12928.md)
    Dim tableName As String
    Dim columnName As String
    Dim rowIndex As Integer
    Dim rule As String
    Dim comment As String
    Dim value As [ITransaction](topic12837.md)
     
    value = instance.CreateTxSetCalculationTableColumnRowRule(tableName, columnName, rowIndex, rule, comment)  
  
C#|   
---|---  
      
    
    public [ITransaction](topic12837.md) CreateTxSetCalculationTableColumnRowRule( 
       string _tableName_ ,
       string _columnName_ ,
       int _rowIndex_ ,
       string _rule_ ,
       string _comment_
    )  
  
#### Parameters

 _tableName_
    The name of the table to use.
_columnName_
    The name of the column to use.
_rowIndex_
    The row index of the cell to set.
_rule_
    The rule to set in the cell.
_comment_
    The comment to set on the cell.

#### Return Value

A transaction that will perform the operation.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ProjectTransactionFactory Class](topic12928.md)   
[ProjectTransactionFactory Members](topic12929.md)

©2024 DriveWorks Ltd. All Rights Reserved.
