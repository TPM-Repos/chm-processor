![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
WriteEntry Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic10377.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Reporting Namespace](topic10334.md) > [CompositeReportWriter Class](topic10363.md) : WriteEntry Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_entryLevel_
    The logging level which applies to to entry.

_entryType_
    The type of entry to write.

_entryClass_
    The class of entry - e.g. "Drive Dimension", useful for filtering.

_entryTarget_
    The target of the entry - e.g. "SomeDimension (D1@Sketch1@SomePart)", useful for filtering.

_entryDescription_
    The description of the entry - e.g. "Driving 'SomeDimension' to 167.8".

_entryDetail_
    Optional additional detail.

Glossary Item Box

Writes a report entry to current process in the report. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Sub WriteEntry( _
       ByVal _entryLevel_ As [ReportingLevel](topic10362.md), _
       ByVal _entryType_ As [ReportEntryType](topic10361.md), _
       ByVal _entryClass_ As String, _
       ByVal _entryTarget_ As String, _
       ByVal _entryDescription_ As String, _
       ByVal _entryDetail_ As String _
    )   
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [CompositeReportWriter](topic10363.md)
    Dim entryLevel As [ReportingLevel](topic10362.md)
    Dim entryType As [ReportEntryType](topic10361.md)
    Dim entryClass As String
    Dim entryTarget As String
    Dim entryDescription As String
    Dim entryDetail As String
     
    instance.WriteEntry(entryLevel, entryType, entryClass, entryTarget, entryDescription, entryDetail)  
  
C#|   
---|---  
      
    
    public void WriteEntry( 
       [ReportingLevel](topic10362.md) _entryLevel_ ,
       [ReportEntryType](topic10361.md) _entryType_ ,
       string _entryClass_ ,
       string _entryTarget_ ,
       string _entryDescription_ ,
       string _entryDetail_
    )  
  
#### Parameters

 _entryLevel_
    The logging level which applies to to entry.
_entryType_
    The type of entry to write.
_entryClass_
    The class of entry - e.g. "Drive Dimension", useful for filtering.
_entryTarget_
    The target of the entry - e.g. "SomeDimension (D1@Sketch1@SomePart)", useful for filtering.
_entryDescription_
    The description of the entry - e.g. "Driving 'SomeDimension' to 167.8".
_entryDetail_
    Optional additional detail.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[CompositeReportWriter Class](topic10363.md)   
[CompositeReportWriter Members](topic10364.md)

©2024 DriveWorks Ltd. All Rights Reserved.
