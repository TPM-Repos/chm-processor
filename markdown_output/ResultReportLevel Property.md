ResultReportLevel Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.EventFlow Namespace](topic6871.md) > [ExecutableNodeBase Class](topic6938.md) : ResultReportLevel Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets the reporting level to use when writing the result of this node to the report. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Protected ReadOnly Property ResultReportLevel As Nullable(Of ReportingLevel)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ExecutableNodeBase](topic6938.md)
    Dim value As Nullable(Of ReportingLevel)
     
    value = instance.ResultReportLevel  
  
C#|   
---|---  
      
    
    protected Nullable<ReportingLevel> ResultReportLevel {get;}  
  
# Remarks

If this is not set the default level will be used which depends on the final state of the node.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ExecutableNodeBase Class](topic6938.md)   
[ExecutableNodeBase Members](topic6939.md)


