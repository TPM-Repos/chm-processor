SolidWorks Property   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks Namespace](topic13345.md) > [ISolidWorksService Interface](topic13411.md) : SolidWorks Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets the current instance of SolidWorks, or a null reference (Nothing in Visual Basic) if the application is not connected to SolidWorks. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    ReadOnly Property SolidWorks As Object  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ISolidWorksService](topic13411.md)
    Dim value As Object
     
    value = instance.SolidWorks  
  
C#|   
---|---  
      
    
    object SolidWorks {get;}  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ISolidWorksService Interface](topic13411.md)   
[ISolidWorksService Members](topic13412.md)


