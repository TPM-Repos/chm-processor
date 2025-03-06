![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
DataExportSummaryInfo Constructor   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic2650.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [DataExportSummaryInfo Class](topic2644.md) : DataExportSummaryInfo Constructor  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_summaryType_
    

_rowDefinition_
    

_message_
    

_values_
    

Glossary Item Box

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _summaryType_ As [DataExportSummaryType](topic2347.md), _
       ByVal _rowDefinition_ As [DataExportRowDefinition](topic2635.md), _
       ByVal _message_ As String, _
       ByVal _values_ As IDictionary(Of String,String) _
    )  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim summaryType As [DataExportSummaryType](topic2347.md)
    Dim rowDefinition As [DataExportRowDefinition](topic2635.md)
    Dim message As String
    Dim values As IDictionary(Of String,String)
     
    Dim instance As New [DataExportSummaryInfo](topic2644.md)(summaryType, rowDefinition, message, values)  
  
C#|   
---|---  
      
    
    public DataExportSummaryInfo( 
       [DataExportSummaryType](topic2347.md) _summaryType_ ,
       [DataExportRowDefinition](topic2635.md) _rowDefinition_ ,
       string _message_ ,
       IDictionary<string,string> _values_
    )  
  
#### Parameters

 _summaryType_
    
_rowDefinition_
    
_message_
    
_values_
    

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[DataExportSummaryInfo Class](topic2644.md)   
[DataExportSummaryInfo Members](topic2645.md)

©2024 DriveWorks Ltd. All Rights Reserved.
