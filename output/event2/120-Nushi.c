v o i d   e n t r y p o i n t _ 1 2 0 _ 2 0 ( )   {  
 	 s t a r t ( )  
 	 p r i n t f ( " I ' m   u n l o a d i n g   t h i s   c a r g o   o f   p u m p k i n \ n s o u p   h e r e . \ n \ n \ n Y o u ' v e   p i c k e d   a n   o d d   p l a c e   f o r \ n s o u p   d e l i v e r y .   F e e l s   d a n g e r o u s . \ n S o m e t h i n g   c o u l d   j u m p   o u t   a t   u s   a t   a n y \ n m o m e n t ,   h u n g r y   f o r   s o u p . . . o r   r o b o t . " )  
 }  
  
 v o i d   e n t r y p o i n t _ 1 2 0 _ 2 1 ( )   {  
 	 s t a r t ( )  
 	 p r i n t f ( " I ' m   o u t   o f   h e r e !   S e e   y o u   a r o u n d ,   z z z r t ! # # # # ( " )  
 	 s t o r y _ f l a g s [ 3 6 6   0 x 0 1 6 E ]   =   t r u e ;  
 	 s t o r y _ f l a g s [ 3 6 8   0 x 0 1 7 0 ]   =   t r u e ;  
 	 s t o r y _ f l a g s [ 2 8 8   0 x 0 1 2 0 ]   =   t r u e ;  
 }  
  
 v o i d   e n t r y p o i n t _ 1 2 0 _ 0 1 ( )   {  
 	 s t a r t ( )  
 	 s w i t c h   ( s t o r y _ f l a g s [ 1 7   0 x 0 0 1 1 ] )   {  
 	     c a s e   0 :  
 	 	 p r i n t f ( " H o   h o h o !   S o   y o u   n o w   h o l d   t h e \ n T r i f o r c e ,   d o   y o u ?   A s t o n i s h i n g ! " )  
 	 	 f l w _ 3 5 :  
 	 	 p r i n t f ( " Y o u   k n o w   w h a t   y o u   m u s t   d o .   G o ,   a n d \ n d o   n o t   s t r a y   f r o m   t h e   p a t h   y o u   k n o w \ n y o u   m u s t   w a l k . " )  
 	 	 f l w _ 3 6 :  
 	 	 O r d e r e d D i c t ( [ ( ' t y p e ' ,   ' t y p e 3 ' ) ,   ( ' s u b T y p e ' ,   1 ) ,   ( ' p a r a m 1 ' ,   3 ) ,   ( ' p a r a m 2 ' ,   - 1 ) ,   ( ' n e x t ' ,   - 1 ) ,   ( ' p a r a m 3 ' ,   4 2 ) ] )  
 	     c a s e   1 :  
 	 	 s w i t c h   ( s t o r y _ f l a g s [ 2 2   0 x 0 0 1 6 ] )   {  
 	 	     c a s e   0 :  
 	 	 	 p r i n t f ( " H o   h o !   A s t o n i s h i n g .   I   s e e   y o u ' v e   f i n a l l y \ n f o u n d   t h e   l o c a t i o n   o f   t h e   T r i f o r c e ! " )  
 	 	 	 g o t o   f l w _ 3 5  
 	 	     c a s e   1 :  
 	 	 	 s w i t c h   ( s t o r y _ f l a g s [ 3 6 9   0 x 0 1 7 1 ] )   {  
 	 	 	     c a s e   0 :  
 	 	 	 	 p r i n t f ( " S u r e l y   y o u   u n d e r s t a n d   w h a t   y o u   n e e d \ n t o   d o   n o w .   T h e   s o n g   o p e n s   a   d o o r w a y \ n t o   a   t r i a l .   T h e   e n t r a n c e   t o   i t   i s   h i d d e n \ n s o m e w h e r e   # " )  
 	 	 	 	 g o t o   f l w _ 3 6  
 	 	 	     c a s e   1 :  
 	 	 	 	 s w i t c h   ( s t o r y _ f l a g s [ 1 9   0 x 0 0 1 3 ] )   {  
 	 	 	 	     c a s e   0 :  
 	 	 	 	 	 s w i t c h   ( s t o r y _ f l a g s [ 1 6   0 x 0 0 1 0 ] )   {  
 	 	 	 	 	     c a s e   0 :  
 	 	 	 	 	 	 s w i t c h   ( s t o r y _ f l a g s [ 2 1   0 x 0 0 1 5 ] )   {  
 	 	 	 	 	 	     c a s e   0 :  
 	 	 	 	 	 	 	 O r d e r e d D i c t ( [ ( ' t y p e ' ,   ' t y p e 3 ' ) ,   ( ' s u b T y p e ' ,   0 ) ,   ( ' p a r a m 1 ' ,   0 ) ,   ( ' p a r a m 2 ' ,   2 0 ) ,   ( ' n e x t ' ,   1 3 ) ,   ( ' p a r a m 3 ' ,   6 ) ] )  
 	 	 	 	 	 	 	 c h a n g e S c e n e ( 5 ,   0 )   / /    
 	 	 	 	 	 	     c a s e   1 :  
 	 	 	 	 	 	 	 f l w _ 8 :  
 	 	 	 	 	 	 	 p r i n t f ( " H o - h o h o h o !   H o w   g o e s   y o u r   q u e s t ,   b o y ? \ n \ n \ n \ n Y o u   m u s t   l e a r n   t h e   t h r e e   p a r t s   o f   t h e \ n t h e   S o n g   o f   t h e   H e r o   k n o w n   t o   t h e \ n d r a g o n s   a n d   t h e n   r e t u r n   t o   m e \ n o n c e   m o r e ! \ n T h e   d r a g o n s   r e s i d e   i n   F a r o n   W o o d s , \ n E l d i n   V o l c a n o ,   a n d   L a n a y r u   D e s e r t . \ n G o   a n d   f i n d   t h o s e   d r a g o n s ! " )  
 	 	 	 	 	 	 }  
 	 	 	 	 	     c a s e   1 :  
 	 	 	 	 	 	 g o t o   f l w _ 8  
 	 	 	 	 	 }  
 	 	 	 	     c a s e   1 :  
 	 	 	 	 	 s w i t c h   ( s t o r y _ f l a g s [ 2 0 0   0 x 0 0 C 8 ] )   {  
 	 	 	 	 	     c a s e   0 :  
 	 	 	 	 	 	 p r i n t f ( " G a t h e r   t h e   p a r t s   o f   t h e   S o n g   o f   t h e \ n H e r o   f r o m   t h e   t h r e e   d r a g o n s \ n a n d   t h e n   r e t u r n   t o   m e . \ n \ n T h e n   I   s h a l l   c o m p l e t e   t h e   t u n e   w i t h \ n m y   o w n   p e r f o r m a n c e ! \ n \ n \ n # # # # # I t ' s   b e e n   q u i t e   a   w h i l e   s i n c e   I   l a s t   s a n g . \ n A h e m - h e m . . .   I   d o   b e l i e v e   s o m e   v o c a l \ n e x e r c i s e s   a r e   i n   o r d e r . . . # # # # # " )  
 	 	 	 	 	     c a s e   1 :  
 	 	 	 	 	 	 p r i n t f ( " T e l l   m e ,   b o y ,   w a s   i t   y o u   w h o   b r o u g h t \ n m e   t h i s   m o s t   d e l e c t a b l e   c a u l d r o n \ n o f   p u m p k i n   s o u p ? \ n \ n I   m u s t   a p o l o g i z e   f o r   m y   e a r l i e r \ n b e h a v i o r .   A   m o s t   p e c u l i a r   a n d   i r k s o m e \ n p e s t   p o s s e s s e d   m e .   I   w a s   n o t   m y s e l f . \ n \ n B u t   t h a t   b u s i n e s s   i s   d o n e   w i t h   n o w ! \ n T h e   d e l i c i o u s   a r o m a   o f   t h a t   s o u p \ n h a s   r e s t o r e d   m e   t o   m y   s e n s e s . " )  
 	 	 	 	 	 	 p r i n t f ( " I   a m   t h e   g r e a t   s p i r i t   t h e y   c a l l   L e v i a s . \ n B e f o r e   s h e   p a s s e d   f r o m   t h i s   w o r l d   s o \ n l o n g   a g o ,   t h e   g o d d e s s ,   H y l i a ,   a p p o i n t e d \ n m e   a s   w a r d e n   o f   t h e   s k i e s . \ n A n d   w h a t   d o   t h e y   c a l l   y o u ,   b o y ? # # # # # \ n A h ,   # # " )  
 	 	 	 	 	 	 s w i t c h   ( O r d e r e d D i c t ( [ ( ' t y p e ' ,   ' s w i t c h ' ) ,   ( ' s u b T y p e ' ,   6 ) ,   ( ' p a r a m 2 ' ,   0 ) ,   ( ' p a r a m 3 ' ,   0 ) ,   ( ' p a r a m 4 ' ,   2 ) ,   ( ' p a r a m 5 ' ,   0 ) ] ) )   {  
 	 	 	 	 	 	     c a s e   0 :  
 	 	 	 	 	 	 	 f l w _ 4 :  
 	 	 	 	 	 	 	 p r i n t f ( " A s   I   s u s p e c t e d . . . # # # # #   L i s t e n   c l o s e l y ,   a n d \ n I   w i l l   t e l l   y o u . \ n \ n \ n A s   y o u   l i k e l y   k n o w ,   l o n g   a g o ,   a n   e v i l \ n f o r c e   a t t e m p t e d   t o   t a k e   t h e   T r i f o r c e \ n f o r   h i s   o w n . \ n \ n T h e   g o d d e s s   d i d   e v e r y t h i n g   i n   h e r \ n p o w e r   t o   p r e v e n t   i t   f r o m   f a l l i n g \ n i n t o   h i s   h a n d s . \ n \ n F o r   t h e   s a f e t y   o f   a l l   t h i n g s ,   s h e   h i d \ n t h e   T r i f o r c e   s o m e w h e r e   w i t h i n   t h e \ n r o c k   y o u   c a l l   S k y l o f t .   H o w e v e r ,   i t s \ n l o c a t i o n   h a s   b e e n   k e p t   s e c r e t .   \ n E v e n   I   d o   n o t   k n o w   w h e r e   i t   r e s t s   n o w . \ n O h ,   b u t   t h e   g o d d e s s   d i d   e n t r u s t   m e \ n w i t h   a   h i n t   a s   t o   t h e   T r i f o r c e ' s   l o c a t i o n . \ n \ n T h e   c l u e   i s   a   s o n g ,   m e a n t   t o   b e   p l a y e d \ n o n   t h e   h a r p   y o u   h o l d .   I t   i s   k n o w n   a s   t h e \ n # " )  
 	 	 	 	 	 	 	 p r i n t f ( " T h e   s o n g   i s   t h e   # " )  
 	 	 	 	 	 	 	 p r i n t f ( " T h e   g o d d e s s   s p l i t   t h i s   s o n g   i n t o   f o u r \ n p a r t s .   S h e   e n t r u s t e d   o n e   p a r t   t o   m e \ n a n d   t h e   o t h e r   t h r e e   t o   t h e   d r a g o n s \ n o f   t h e   l a n d . \ n Y o u   m u s t   g a t h e r   e a c h   o f   t h e   # " )  
 	 	 	 	 	 	 	 s t o r y _ f l a g s [ 2 0 0   0 x 0 0 C 8 ]   =   t r u e ;  
 	 	 	 	 	 	 	 s t o r y _ f l a g s [ 1 6 9   0 x 0 0 A 9 ]   =   t r u e ;  
 	 	 	 	 	 	 	 s t o r y _ f l a g s [ 7 8 1   0 x 0 3 0 D ]   =   t r u e ;  
 	 	 	 	 	 	     c a s e   1 :  
 	 	 	 	 	 	 	 p r i n t f ( " D o   I   k n o w ?   Y o u   d o   r e a l i z e   y o u   a r e   \ n s p e a k i n g   t o   t h e   g r e a t   s k y   s p i r i t , \ n d o   y o u   n o t ?   # # # # # B a h h h .   N o   m a t t e r . " )  
 	 	 	 	 	 	 	 g o t o   f l w _ 4  
 	 	 	 	 	 	 }  
 	 	 	 	 	 }  
 	 	 	 	 }  
 	 	 	 }  
 	 	 }  
 	 }  
 }  
  
 v o i d   e n t r y p o i n t _ 1 2 0 _ 0 2 ( )   {  
 	 s t a r t ( )  
 	 s w i t c h   ( O r d e r e d D i c t ( [ ( ' t y p e ' ,   ' s w i t c h ' ) ,   ( ' s u b T y p e ' ,   6 ) ,   ( ' p a r a m 2 ' ,   3 6 ) ,   ( ' p a r a m 3 ' ,   6 ) ,   ( ' p a r a m 4 ' ,   2 ) ,   ( ' p a r a m 5 ' ,   1 2 ) ] ) )   {  
 	     c a s e   0 :  
 	 	 s c e n e _ f l a g s [ 2 1   ' T h e   S k y ' ] [ 3 7   0 x 2 5 ]   =   t r u e ;  
 	     c a s e   1 :  
 	 	 s c e n e _ f l a g s [ 2 1   ' T h e   S k y ' ] [ 3 6   0 x 2 4 ]   =   t r u e ;  
 	 }  
 }  
  
 