![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateReportWriter Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic10360.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Reporting Namespace](topic10334.md) > [IReportWriterFactory Interface](topic10355.md) : CreateReportWriter Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_title_
    

Glossary Item Box

Creates a new report writer. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Function CreateReportWriter( _
       ByVal _title_ As String _
    ) As [IReportWriter](topic10344.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [IReportWriterFactory](topic10355.md)
    Dim title As String
    Dim value As [IReportWriter](topic10344.md)
     
    value = instance.CreateReportWriter(title)  
  
C#|   
---|---  
      
    
    [IReportWriter](topic10344.md) CreateReportWriter( 
       string _title_
    )  
  
#### Parameters

 _title_
    

#### Return Value

The newly created report writer.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[IReportWriterFactory Interface](topic10355.md)   
[IReportWriterFactory Members](topic10356.md)

©2024 DriveWorks Ltd. All Rights Reserved.
