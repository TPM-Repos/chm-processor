Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
IPreviewHost Interface   
[Members](topic7281.md)   
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Forms Namespace](topic7266.md) : IPreviewHost Interface  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Provides a contract to a host responsible for translating an [EffectivePreviewResult](topic8075.md). See remarks for details. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Interface IPreviewHost   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IPreviewHost](topic7280.md)  
  
C#|   
---|---  
      
    
    public interface IPreviewHost   
  
# Remarks

Implementations of this contract should be added as a service to the System.IServiceProvider held by the **DriveWorks.Hosting.EngineHost**.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IPreviewHost Members](topic7281.md)   
[DriveWorks.Forms Namespace](topic7266.md)


