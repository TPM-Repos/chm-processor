Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetObjectData Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) > [TransitionEventArgs Class](topic11776.md) : GetObjectData Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_info_
    

_context_
    

Glossary Item Box

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Protected Sub GetObjectData( _
       ByVal _info_ As SerializationInfo, _
       ByVal _context_ As StreamingContext _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [TransitionEventArgs](topic11776.md)
    Dim info As SerializationInfo
    Dim context As StreamingContext
     
    instance.GetObjectData(info, context)  
  
C#|   
---|---  
      
    
    protected void GetObjectData( 
       SerializationInfo _info_ ,
       StreamingContext _context_
    )  
  
#### Parameters

 _info_
    
_context_
    

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[TransitionEventArgs Class](topic11776.md)   
[TransitionEventArgs Members](topic11777.md)


