       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
WriteEntry Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic10506.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Reporting Namespace](topic10334.md) > [TraceReportWriter Class](topic10494.md) : WriteEntry Method  
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

# Syntax

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
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [TraceReportWriter](topic10494.md)
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

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[TraceReportWriter Class](topic10494.md)   
[TraceReportWriter Members](topic10495.md)

©2024 DriveWorks Ltd. All Rights Reserved.
