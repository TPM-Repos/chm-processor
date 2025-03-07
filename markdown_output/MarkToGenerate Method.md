Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
MarkToGenerate Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [GroupReleasedComponents Class](topic3238.md) : MarkToGenerate Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_componentTargetPath_
    The full path to the released component to update.

Glossary Item Box

Marks the specified component as requiring generation. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Sub MarkToGenerate( _
       ByVal _componentTargetPath_ As String _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [GroupReleasedComponents](topic3238.md)
    Dim componentTargetPath As String
     
    instance.MarkToGenerate(componentTargetPath)  
  
C#|   
---|---  
      
    
    public void MarkToGenerate( 
       string _componentTargetPath_
    )  
  
#### Parameters

 _componentTargetPath_
    The full path to the released component to update.

# Remarks

Marking a component as requiring generation clears the generating, generated, and failed fields.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[GroupReleasedComponents Class](topic3238.md)   
[GroupReleasedComponents Members](topic3239.md)


