SetChosenFields Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [SqlServerDataTable Class](topic5396.md) : SetChosenFields Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_fieldsToSet_
    

Glossary Item Box

Sets the chosen fields for this table. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Sub SetChosenFields( _
       ByVal _fieldsToSet_() As String _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [SqlServerDataTable](topic5396.md)
    Dim fieldsToSet() As String
     
    instance.SetChosenFields(fieldsToSet)  
  
C#|   
---|---  
      
    
    public void SetChosenFields( 
       string[] _fieldsToSet_
    )  
  
#### Parameters

 _fieldsToSet_
    

# Remarks

Will set [AllFields](topic5408.md) to false.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[SqlServerDataTable Class](topic5396.md)   
[SqlServerDataTable Members](topic5397.md)


