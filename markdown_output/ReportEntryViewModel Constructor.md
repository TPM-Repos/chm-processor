       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ReportEntryViewModel Constructor   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic15369.md)  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks.Generation.Unified.UI.ReportViewer Namespace](topic15361.md) > [ReportEntryViewModel Class](topic15363.md) : ReportEntryViewModel Constructor  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_description_
    

_detail_
    

_depth_
    

_type_
    

_process_
    

Glossary Item Box

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _description_ As String, _
       ByVal _detail_ As String, _
       ByVal _depth_ As Integer, _
       ByVal _type_ As [ReportEntryType](topic10361.md), _
       ByVal _process_ As [ReportProcessViewModel](topic15390.md) _
    )  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim description As String
    Dim detail As String
    Dim depth As Integer
    Dim type As [ReportEntryType](topic10361.md)
    Dim process As [ReportProcessViewModel](topic15390.md)
     
    Dim instance As New [ReportEntryViewModel](topic15363.md)(description, detail, depth, type, process)  
  
C#|   
---|---  
      
    
    public ReportEntryViewModel( 
       string _description_ ,
       string _detail_ ,
       int _depth_ ,
       [ReportEntryType](topic10361.md) _type_ ,
       [ReportProcessViewModel](topic15390.md) _process_
    )  
  
#### Parameters

 _description_
    
_detail_
    
_depth_
    
_type_
    
_process_
    

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ReportEntryViewModel Class](topic15363.md)   
[ReportEntryViewModel Members](topic15364.md)

©2024 DriveWorks Ltd. All Rights Reserved.
