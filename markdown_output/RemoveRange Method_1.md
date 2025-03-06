RemoveRange Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [WordDocument Class](topic5885.md) : RemoveRange Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_name_
    Name of the range to be removed from the drive list.

Glossary Item Box

Removes a bookmark from the list of ranges to be driven. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Sub RemoveRange( _
       ByVal _name_ As String _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [WordDocument](topic5885.md)
    Dim name As String
     
    instance.RemoveRange(name)  
  
C#|   
---|---  
      
    
    public void RemoveRange( 
       string _name_
    )  
  
#### Parameters

 _name_
    Name of the range to be removed from the drive list.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[WordDocument Class](topic5885.md)   
[WordDocument Members](topic5886.md)


