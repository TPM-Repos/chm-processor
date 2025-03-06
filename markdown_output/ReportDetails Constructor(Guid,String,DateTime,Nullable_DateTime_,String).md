ReportDetails Constructor(Guid,String,DateTime,Nullable<DateTime>,String)   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ReportDetails Class](topic5221.md) > [ReportDetails Constructor](topic5227.md) : ReportDetails Constructor(Guid,String,DateTime,Nullable<DateTime>,String)  
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

Glossary Item Box

Initializes a new instance of the [ReportDetails](topic5221.md) class. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _id_ As Guid, _
       ByVal _title_ As String, _
       ByVal _dateStarted_ As Date, _
       ByVal _dateCompleted_ As Nullable(Of Date), _
       ByVal _path_ As String _
    )  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim id As Guid
    Dim title As String
    Dim dateStarted As Date
    Dim dateCompleted As Nullable(Of Date)
    Dim path As String
     
    Dim instance As New [ReportDetails](topic5221.md)(id, title, dateStarted, dateCompleted, path)  
  
C#|   
---|---  
      
    
    public ReportDetails( 
       Guid _id_ ,
       string _title_ ,
       DateTime _dateStarted_ ,
       Nullable<DateTime> _dateCompleted_ ,
       string _path_
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

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ReportDetails Class](topic5221.md)   
[ReportDetails Members](topic5222.md)   
[Overload List](topic5227.md)


