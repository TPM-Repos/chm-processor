Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
AdditionalFileFormatGenerationFailed Event   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks.Generation Namespace](topic15094.md) > [ICommonGenerationContext Interface](topic15096.md) : AdditionalFileFormatGenerationFailed Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised when the generation of an additional file format fails. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Event AdditionalFileFormatGenerationFailed As EventHandler(Of FileFormatGenerationExceptionEventArgs)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ICommonGenerationContext](topic15096.md)
    Dim handler As EventHandler(Of FileFormatGenerationExceptionEventArgs)
     
    AddHandler instance.AdditionalFileFormatGenerationFailed, handler  
  
C#|   
---|---  
      
    
    event EventHandler<FileFormatGenerationExceptionEventArgs> AdditionalFileFormatGenerationFailed  
  
# Event Data

The event handler receives an argument of type [FileFormatGenerationExceptionEventArgs](topic15210.md) containing data related to this event. The following **FileFormatGenerationExceptionEventArgs** properties provide information specific to this event.

Property| Description  
---|---  
[Exception](topic813.md)| Gets the exception to which the event refers. (Inherited from [DriveWorks.Applications.ExceptionEventArgs](topic806.md))  
[TargetPath](topic15217.md)| Gets the target path.   
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ICommonGenerationContext Interface](topic15096.md)   
[ICommonGenerationContext Members](topic15097.md)


