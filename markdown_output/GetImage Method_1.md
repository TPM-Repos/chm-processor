Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetImage Method   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [ICommandMonitor Interface](topic158.md) : GetImage Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_context_
    The context which would be passed to the command's invoke method.

Glossary Item Box

Gets the context-specific image which represents the command. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Function GetImage( _
       ByVal _context_ As Object _
    ) As [ImageHandle](topic854.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ICommandMonitor](topic158.md)
    Dim context As Object
    Dim value As [ImageHandle](topic854.md)
     
    value = instance.GetImage(context)  
  
C#|   
---|---  
      
    
    [ImageHandle](topic854.md) GetImage( 
       object _context_
    )  
  
#### Parameters

 _context_
    The context which would be passed to the command's invoke method.

#### Return Value

An image handle representing the image to be shown wherever the command is used in UI elements.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ICommandMonitor Interface](topic158.md)   
[ICommandMonitor Members](topic159.md)


