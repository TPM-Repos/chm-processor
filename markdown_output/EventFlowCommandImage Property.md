Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
EventFlowCommandImage Property   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications.Administrator.Extensibility Namespace](topic1277.md) > [IEventFlowPropertyEditor Interface](topic1279.md) : EventFlowCommandImage Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

The image for the command that should be used inside Event Flow. If this is null then the default folder image will be used in Event Flow. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    ReadOnly Property EventFlowCommandImage As Image  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IEventFlowPropertyEditor](topic1279.md)
    Dim value As Image
     
    value = instance.EventFlowCommandImage  
  
C#|   
---|---  
      
    
    Image EventFlowCommandImage {get;}  
  
# Remarks

This is used when the property is based on a rule.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IEventFlowPropertyEditor Interface](topic1279.md)   
[IEventFlowPropertyEditor Members](topic1280.md)


