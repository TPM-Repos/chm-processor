Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
AdditionalFileFormatPreparing Event   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks.Generation Namespace](topic15094.md) > [ICommonGenerationContext Interface](topic15096.md) : AdditionalFileFormatPreparing Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised when an additional format is being prepared for generation. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Event AdditionalFileFormatPreparing As EventHandler(Of FileFormatGenerationEventArgs)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ICommonGenerationContext](topic15096.md)
    Dim handler As EventHandler(Of FileFormatGenerationEventArgs)
     
    AddHandler instance.AdditionalFileFormatPreparing, handler  
  
C#|   
---|---  
      
    
    event EventHandler<FileFormatGenerationEventArgs> AdditionalFileFormatPreparing  
  
# Event Data

The event handler receives an argument of type [FileFormatGenerationEventArgs](topic15202.md) containing data related to this event. The following **FileFormatGenerationEventArgs** properties provide information specific to this event.

Property| Description  
---|---  
[TargetPath](topic15209.md)| Gets the target path.   
  
# Remarks

Preparation of an additional file format is mostly checking whether the file already exists.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ICommonGenerationContext Interface](topic15096.md)   
[ICommonGenerationContext Members](topic15097.md)


