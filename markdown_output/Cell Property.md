![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Cell Property   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic5611.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [TableExportRow Class](topic5600.md) : Cell Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_header_
    The column header for the cell to fetch.

Glossary Item Box

Gets a cell with the specified header from this row. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public ReadOnly Default Property Cell( _
       ByVal _header_ As String _
    ) As [TableExportCell](topic5560.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [TableExportRow](topic5600.md)
    Dim header As String
    Dim value As [TableExportCell](topic5560.md)
     
    value = instance.Cell(header)  
  
C#|   
---|---  
      
    
    public [TableExportCell](topic5560.md) this[ 
       string _header_
    ]; {get;}  
  
#### Parameters

 _header_
    The column header for the cell to fetch.

# ![](dotnetimages/collapse.gif)Remarks

If a cell by the specified header does not exist, it will be created.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[TableExportRow Class](topic5600.md)   
[TableExportRow Members](topic5601.md)

©2024 DriveWorks Ltd. All Rights Reserved.
