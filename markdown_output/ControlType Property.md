Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ControlType Property   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [ConfigurablePreviewControlAttribute Class](topic729.md) : ControlType Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets the type of document this control handles. See remarks for details. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public ReadOnly Property ControlType As Type  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ConfigurablePreviewControlAttribute](topic729.md)
    Dim value As Type
     
    value = instance.ControlType  
  
C#|   
---|---  
      
    
    public Type ControlType {get;}  
  
# Remarks

The specified document should be capable of generating a preview. This control will then be used to handle the result of that preview.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ConfigurablePreviewControlAttribute Class](topic729.md)   
[ConfigurablePreviewControlAttribute Members](topic730.md)


