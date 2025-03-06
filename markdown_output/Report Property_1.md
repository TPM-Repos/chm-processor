Report Property   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks Namespace](topic13345.md) > [FileFormatGenerator Class](topic13579.md) : Report Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets/sets the report writer to use during generation process. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Protected Property Report As [IEventReportWriter](topic10336.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [FileFormatGenerator](topic13579.md)
    Dim value As [IEventReportWriter](topic10336.md)
     
    instance.Report = value
     
    value = instance.Report  
  
C#|   
---|---  
      
    
    protected [IEventReportWriter](topic10336.md) Report {get; set;}  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[FileFormatGenerator Class](topic13579.md)   
[FileFormatGenerator Members](topic13580.md)


