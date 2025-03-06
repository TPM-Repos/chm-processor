![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Open Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic10460.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Reporting Namespace](topic10334.md) > [ReportPackage Class](topic10451.md) : Open Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_filePath_
    The full path to the report package to create.

Glossary Item Box

Opens a new report package. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Sub Open( _
       ByVal _filePath_ As String _
    )   
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ReportPackage](topic10451.md)
    Dim filePath As String
     
    instance.Open(filePath)  
  
C#|   
---|---  
      
    
    public void Open( 
       string _filePath_
    )  
  
#### Parameters

 _filePath_
    The full path to the report package to create.

# ![](dotnetimages/collapse.gif)Remarks

The report package will be created immediately, any existing file at the specified location will be overwritten.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ReportPackage Class](topic10451.md)   
[ReportPackage Members](topic10452.md)

©2024 DriveWorks Ltd. All Rights Reserved.
