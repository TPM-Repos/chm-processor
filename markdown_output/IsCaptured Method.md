Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
IsCaptured Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [GroupCapturedComponents Class](topic3022.md) : IsCaptured Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_fileName_
    The fully-qualified path to the component file.

Glossary Item Box

Determines whether the specified file is registered as a captured component in the group. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function IsCaptured( _
       ByVal _fileName_ As String _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [GroupCapturedComponents](topic3022.md)
    Dim fileName As String
    Dim value As Boolean
     
    value = instance.IsCaptured(fileName)  
  
C#|   
---|---  
      
    
    public bool IsCaptured( 
       string _fileName_
    )  
  
#### Parameters

 _fileName_
    The fully-qualified path to the component file.

#### Return Value

True if the component is captured, otherwise false.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[GroupCapturedComponents Class](topic3022.md)   
[GroupCapturedComponents Members](topic3023.md)


