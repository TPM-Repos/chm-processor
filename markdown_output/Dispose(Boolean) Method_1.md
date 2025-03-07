Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Dispose(Boolean) Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Reporting Namespace](topic10334.md) > [ReportWriterBase Class](topic10476.md) : Dispose(Boolean) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_disposing_
    True if the object is undergoing explicit finalization, otherwise false.

Glossary Item Box

Disposes the report writer and flushes its contents to the report. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Protected Overridable Sub Dispose( _
       ByVal _disposing_ As Boolean _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ReportWriterBase](topic10476.md)
    Dim disposing As Boolean
     
    instance.Dispose(disposing)  
  
C#|   
---|---  
      
    
    protected virtual void Dispose( 
       bool _disposing_
    )  
  
#### Parameters

 _disposing_
    True if the object is undergoing explicit finalization, otherwise false.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ReportWriterBase Class](topic10476.md)   
[ReportWriterBase Members](topic10477.md)


