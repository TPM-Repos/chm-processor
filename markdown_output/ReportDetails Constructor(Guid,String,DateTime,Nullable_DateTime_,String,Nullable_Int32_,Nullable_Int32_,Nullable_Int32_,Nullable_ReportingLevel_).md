![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ReportDetails Constructor(Guid,String,DateTime,Nullable<DateTime>,String,Nullable<Int32>,Nullable<Int32>,Nullable<Int32>,Nullable<ReportingLevel>)   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic5230.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ReportDetails Class](topic5221.md) > [ReportDetails Constructor](topic5227.md) : ReportDetails Constructor(Guid,String,DateTime,Nullable<DateTime>,String,Nullable<Int32>,Nullable<Int32>,Nullable<Int32>,Nullable<ReportingLevel>)  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_id_
    The unique identifier of the report.

_title_
    The title of the report.

_dateStarted_
    The date the report was started.

_dateCompleted_
    The date the report was completed.

_path_
    The path to the report if it is a legacy DriveWorks 6 report.

_informationCount_
    The number of information entries in the report.

_warningCount_
    The number of warning entries in the report.

_errorCount_
    The number of error entries in the report.

_reportingLevel_
    The reporting level of the report.

Glossary Item Box

Initializes a new instance of the [ReportDetails](topic5221.md) class. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _id_ As Guid, _
       ByVal _title_ As String, _
       ByVal _dateStarted_ As Date, _
       ByVal _dateCompleted_ As Nullable(Of Date), _
       ByVal _path_ As String, _
       ByVal _informationCount_ As Nullable(Of Integer), _
       ByVal _warningCount_ As Nullable(Of Integer), _
       ByVal _errorCount_ As Nullable(Of Integer), _
       ByVal _reportingLevel_ As Nullable(Of ReportingLevel) _
    )  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim id As Guid
    Dim title As String
    Dim dateStarted As Date
    Dim dateCompleted As Nullable(Of Date)
    Dim path As String
    Dim informationCount As Nullable(Of Integer)
    Dim warningCount As Nullable(Of Integer)
    Dim errorCount As Nullable(Of Integer)
    Dim reportingLevel As Nullable(Of ReportingLevel)
     
    Dim instance As New [ReportDetails](topic5221.md)(id, title, dateStarted, dateCompleted, path, informationCount, warningCount, errorCount, reportingLevel)  
  
C#|   
---|---  
      
    
    public ReportDetails( 
       Guid _id_ ,
       string _title_ ,
       DateTime _dateStarted_ ,
       Nullable<DateTime> _dateCompleted_ ,
       string _path_ ,
       Nullable<int> _informationCount_ ,
       Nullable<int> _warningCount_ ,
       Nullable<int> _errorCount_ ,
       Nullable<ReportingLevel> _reportingLevel_
    )  
  
#### Parameters

 _id_
    The unique identifier of the report.
_title_
    The title of the report.
_dateStarted_
    The date the report was started.
_dateCompleted_
    The date the report was completed.
_path_
    The path to the report if it is a legacy DriveWorks 6 report.
_informationCount_
    The number of information entries in the report.
_warningCount_
    The number of warning entries in the report.
_errorCount_
    The number of error entries in the report.
_reportingLevel_
    The reporting level of the report.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ReportDetails Class](topic5221.md)   
[ReportDetails Members](topic5222.md)   
[Overload List](topic5227.md)

©2024 DriveWorks Ltd. All Rights Reserved.
