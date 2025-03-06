![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
AddCommonColumn Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [IDataExportDefinition Interface](topic2177.md) : AddCommonColumn Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_name_
    The name of this column.

_type_
    The data type for this column.

_commonRule_
    The common rule to set for this column.

_commonComment_
    The common comment to set for this column.

Glossary Item Box

Adds a common column to the document. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Function AddCommonColumn( _
       ByVal _name_ As String, _
       ByVal _type_ As String, _
       ByVal _commonRule_ As String, _
       ByVal _commonComment_ As String _
    ) As DataExportColumnDefinition  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [IDataExportDefinition](topic2177.md)
    Dim name As String
    Dim type As String
    Dim commonRule As String
    Dim commonComment As String
    Dim value As DataExportColumnDefinition
     
    value = instance.AddCommonColumn(name, type, commonRule, commonComment)  
  
C#|   
---|---  
      
    
    DataExportColumnDefinition AddCommonColumn( 
       string _name_ ,
       string _type_ ,
       string _commonRule_ ,
       string _commonComment_
    )  
  
#### Parameters

 _name_
    The name of this column.
_type_
    The data type for this column.
_commonRule_
    The common rule to set for this column.
_commonComment_
    The common comment to set for this column.

#### Return Value

Returns the added column.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[IDataExportDefinition Interface](topic2177.md)   
[IDataExportDefinition Members](topic2178.md)


