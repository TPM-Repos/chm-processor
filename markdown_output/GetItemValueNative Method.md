![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetItemValueNative Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectListItemData Class](topic4555.md) : GetItemValueNative Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_columnName_
    The name of the column for which to retrieve the value.

Glossary Item Box

Retrieves the item value for the specified column name. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function GetItemValueNative( _
       ByVal _columnName_ As String _
    ) As Object  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ProjectListItemData](topic4555.md)
    Dim columnName As String
    Dim value As Object
     
    value = instance.GetItemValueNative(columnName)  
  
C#|   
---|---  
      
    
    public object GetItemValueNative( 
       string _columnName_
    )  
  
#### Parameters

 _columnName_
    The name of the column for which to retrieve the value.

#### Return Value

Nothing if a column matching that name doesn't exist, otherwise the value for the column.

# ![](dotnetimages/collapse.gif)Remarks

This will perform a case-insensitive search for the column.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ProjectListItemData Class](topic4555.md)   
[ProjectListItemData Members](topic4556.md)


