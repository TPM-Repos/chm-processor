Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Load(Stream) Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ReleasedEmail Class](topic5098.md) > [Load Method](topic5106.md) : Load(Stream) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_stream_
    The stream to deserialize and read the information from.

Glossary Item Box

Reads the information stored about the email from the specified stream. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Sub Load( _
       ByVal _stream_ As Stream _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ReleasedEmail](topic5098.md)
    Dim stream As Stream
     
    instance.Load(stream)  
  
C#|   
---|---  
      
    
    public void Load( 
       Stream _stream_
    )  
  
#### Parameters

 _stream_
    The stream to deserialize and read the information from.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ReleasedEmail Class](topic5098.md)   
[ReleasedEmail Members](topic5099.md)   
[Overload List](topic5106.md)


