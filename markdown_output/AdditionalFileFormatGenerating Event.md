Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
AdditionalFileFormatGenerating Event   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks.Generation Namespace](topic15094.md) > [ICommonGenerationContext Interface](topic15096.md) : AdditionalFileFormatGenerating Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised when an additional file format is about to be generated. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Event AdditionalFileFormatGenerating As EventHandler(Of FileFormatGenerationEventArgs)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ICommonGenerationContext](topic15096.md)
    Dim handler As EventHandler(Of FileFormatGenerationEventArgs)
     
    AddHandler instance.AdditionalFileFormatGenerating, handler  
  
C#|   
---|---  
      
    
    event EventHandler<FileFormatGenerationEventArgs> AdditionalFileFormatGenerating  
  
# Event Data

The event handler receives an argument of type [FileFormatGenerationEventArgs](topic15202.md) containing data related to this event. The following **FileFormatGenerationEventArgs** properties provide information specific to this event.

Property| Description  
---|---  
[TargetPath](topic15209.md)| Gets the target path.   
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ICommonGenerationContext Interface](topic15096.md)   
[ICommonGenerationContext Members](topic15097.md)


